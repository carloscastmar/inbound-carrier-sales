from fastapi import FastAPI
from api.models import VerifyCarrierRequest, VerifyCarrierResponse
from api.services.carrier_verification import verify_carrier_service

app = FastAPI(title="Broker Client API")


@app.post("/verify-carrier", response_model=VerifyCarrierResponse)
def verify_carrier(payload: VerifyCarrierRequest):
    return verify_carrier_service(payload)
