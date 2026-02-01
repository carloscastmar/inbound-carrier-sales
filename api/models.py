from pydantic import BaseModel
from typing import Optional, Literal


class VerifyCarrierRequest(BaseModel):
    mc_number: str
    # identifier_type: Literal["MC", "DOT"]


class VerifyCarrierResponse(BaseModel):
    eligible: bool
    carrier_name: Optional[str]
    operating_status: Optional[str]
    reason: Optional[str]
