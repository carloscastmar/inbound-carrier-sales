from fastapi import FastAPI
from api.models import VerifyCarrierRequest, VerifyCarrierResponse
from api.services.carrier_verification import verify_carrier_service
from api.models import LoadSearchRequest, LoadSearchResponse
from api.services.load_search import search_loads
from api.models import NegotiationConfigRequest, NegotiationConfigResponse
from api.services.negotiation import get_negotiation_config
from api.models import CallRecordRequest, CallRecordResponse
from api.services.call_record import record_call
from api.models import MetricsSummaryResponse
from api.services.metrics import get_metrics_summary

app = FastAPI(title="Broker Client API")


@app.post("/verify-carrier", response_model=VerifyCarrierResponse)
def verify_carrier(payload: VerifyCarrierRequest):
    return verify_carrier_service(payload)

@app.post("/loads/search", response_model=LoadSearchResponse)
def load_search(payload: LoadSearchRequest):
    return search_loads(payload)

@app.post("/negotiation/config", response_model=NegotiationConfigResponse)
def negotiation_config(payload: NegotiationConfigRequest):
    return get_negotiation_config(payload)

@app.post("/calls/record", response_model=CallRecordResponse)
def record_call_endpoint(payload: CallRecordRequest):
    return record_call(payload)

@app.get("/metrics/summary", response_model=MetricsSummaryResponse)
def metrics_summary():
    return get_metrics_summary()