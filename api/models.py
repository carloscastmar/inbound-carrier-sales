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

class LoadSearchRequest(BaseModel):
    origin: Optional[str]
    destination: Optional[str]
    pickup_after: Optional[str]
    equipment_type: Optional[str]
    target_rate: Optional[int]


class Load(BaseModel):
    load_id: str
    origin: str
    destination: str
    pickup_datetime: str
    equipment_type: str
    rate: int
    weight: int
    commodity_type: str


class LoadSearchResponse(BaseModel):
    has_match: bool
    load: Optional[Load] = None