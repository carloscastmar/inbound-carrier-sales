import json
from datetime import datetime
from pathlib import Path
from api.models import LoadSearchRequest, LoadSearchResponse, Load

LOADS_FILE = Path("api/data/loads.json")


def load_data():
    with open(LOADS_FILE) as f:
        return json.load(f)


def matches(load: dict, req: LoadSearchRequest) -> bool:
    if req.origin and req.origin.lower() not in load["origin"].lower():
        return False
    if req.destination and req.destination.lower() not in load["destination"].lower():
        return False
    if req.equipment_type and req.equipment_type != load["equipment_type"]:
        return False
    if req.pickup_after:
        pickup_after = datetime.fromisoformat(req.pickup_after)
        pickup_time = datetime.fromisoformat(load["pickup_datetime"])
        if pickup_time < pickup_after:
            return False
    if req.target_rate > (load["loadboard_rate"] + 150):
        return False
    return True


def search_loads(req: LoadSearchRequest) -> LoadSearchResponse:
    loads = load_data()

    matching = [l for l in loads if matches(l, req)]

    if not matching:
        return LoadSearchResponse(has_match=False)

    # Rank by earliest pickup
    matching.sort(key=lambda l: l["pickup_datetime"])

    best = matching[0]

    return LoadSearchResponse(
        has_match=True,
        load=Load(**best)
    )
