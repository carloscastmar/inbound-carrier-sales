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
    delivery_datetime: str
    equipment_type: str
    loadboard_rate: int
    notes: str
    weight: int
    commodity_type: str
    num_of_pieces: int
    miles: int
    dimensions: str


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


class CallRecordRequest(BaseModel):
    call_id: str
    carrier_mc: Optional[str] = None
    load_id: Optional[str] = None
    initial_rate: Optional[int] = None
    final_rate: Optional[int] = None
    negotiation_rounds: Optional[int] = None
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
    average_difference: float
    average_negotiation_rounds: float
    sentiment_breakdown: Dict[str, int]