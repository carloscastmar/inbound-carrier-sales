import json
from pathlib import Path
from fastapi import HTTPException
from api.models import NegotiationConfigRequest, NegotiationConfigResponse

LOADS_FILE = Path("api/data/loads.json")

BUFFER_AMOUNT = 150
MAX_ROUNDS = 3
COUNTER_STEP = 50


def load_data():
    with open(LOADS_FILE) as f:
        return json.load(f)


def get_negotiation_config(
    payload: NegotiationConfigRequest
) -> NegotiationConfigResponse:
    loads = load_data()

    load = next((l for l in loads if l["load_id"] == payload.load_id), None)

    if not load:
        raise HTTPException(status_code=404, detail="Load not found")

    base_rate = load["loadboard_rate"]
    max_rate = base_rate + BUFFER_AMOUNT

    return NegotiationConfigResponse(
        base_rate=base_rate,
        max_rate=max_rate,
        max_rounds=MAX_ROUNDS,
        counter_step=COUNTER_STEP,
        currency="USD"
    )
