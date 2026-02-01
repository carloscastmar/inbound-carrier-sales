from pydantic import BaseModel
from typing import Optional, Literal
from typing import Dict


class VerifyCarrierRequest(BaseModel):
    mc_number: str
    # identifier_type: Literal["MC", "DOT"]


class VerifyCarrierResponse(BaseModel):
    eligible: bool
    carrier_name: Optional[str]
    operating_status: Optional[str]
    reason: Optional[str]

class LoadSearchRequest(BaseModel):
    origin: Optional[str] = None
    destination: Optional[str] = None
    pickup_after: Optional[str] = None
    equipment_type: Optional[str] = None
    target_rate: Optional[int] = None


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


class NegotiationConfigRequest(BaseModel):
    load_id: str


class NegotiationConfigResponse(BaseModel):
    base_rate: int
    max_rate: int
    max_rounds: int
    counter_step: int
    currency: str

from typing import Optional, Literal


class CallRecordRequest(BaseModel):
    call_id: str
    carrier_mc: str
    load_id: Optional[str] = None
    final_rate: Optional[int] = None
    negotiation_rounds: int
    outcome: Literal["booked", "no_match", "rejected", "transferred"]
    sentiment: Literal["positive", "neutral", "negative"]
    timestamp: str

class CallRecordResponse(BaseModel):
    status: str

class MetricsSummaryResponse(BaseModel):
    total_calls: int
    booked_calls: int
    transferred_calls: int
    no_match_calls: int
    rejected_calls: int
    booking_rate: float
    average_final_rate: float
    average_negotiation_rounds: float
    sentiment_breakdown: Dict[str, int]