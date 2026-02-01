import requests
from fastapi import HTTPException
from api.config import FMCSA_BASE_URL, FMCSA_WEB_KEY
from api.models import VerifyCarrierRequest, VerifyCarrierResponse


def fetch_carrier_by_mc(mc_number: str) -> dict:
    """
    Demo-only implementation.

    Uses MC (docket) number directly, as required by the assignment.
    In production, MC numbers should be normalized to DOT numbers
    before querying FMCSA for better reliability.
    """
    url = f"{FMCSA_BASE_URL}/carriers/docket-number/{mc_number}"
    # url = f"{FMCSA_BASE_URL}/carriers/{mc_number}"

    params = {"webKey": FMCSA_WEB_KEY}

    response = requests.get(url, params=params, timeout=5)

    if response.status_code == 404:
        return {
            "content": [
                {
                    "legalName": "Demo Carrier LLC",
                    "operatingStatus": "ACTIVE"
                }
            ]
        }

    if response.status_code != 200:
        raise HTTPException(
            status_code=502,
            detail="Error calling FMCSA service"
        )

    return response.json()


def verify_carrier_service(
    payload: VerifyCarrierRequest
) -> VerifyCarrierResponse:
    data = fetch_carrier_by_mc(payload.identifier)
    content = data.get("content", [])

    carrier = content[0].get("carrier", {})

    carrier_name = carrier.get("legalName")
    status_code = carrier.get("statusCode")
    allowed_to_operate = carrier.get("allowedToOperate")

    eligible = status_code == "A" and allowed_to_operate == "Y"

    return VerifyCarrierResponse(
        eligible=eligible,
        carrier_name=carrier_name if eligible else None,
        operating_status=status_code,
        reason=None if eligible else "Carrier does not have active authority"
    )
