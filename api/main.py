from fastapi import FastAPI
from api.models import VerifyCarrierRequest, VerifyCarrierResponse
from api.services.carrier_verification import verify_carrier_service
from api.models import LoadSearchRequest, LoadSearchResponse
from api.services.load_search import search_loads

app = FastAPI(title="Broker Client API")


@app.post("/verify-carrier", response_model=VerifyCarrierResponse)
def verify_carrier(payload: VerifyCarrierRequest):
    return verify_carrier_service(payload)

@app.post("/loads/search", response_model=LoadSearchResponse)
def load_search(payload: LoadSearchRequest):
    return search_loads(payload)