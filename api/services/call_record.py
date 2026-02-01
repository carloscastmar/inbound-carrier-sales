import json
from pathlib import Path
from api.models import CallRecordRequest, CallRecordResponse

CALLS_FILE = Path("api/data/calls.json")


def load_calls():
    if not CALLS_FILE.exists():
        return []
    with open(CALLS_FILE) as f:
        return json.load(f)


def save_calls(calls):
    with open(CALLS_FILE, "w") as f:
        json.dump(calls, f, indent=2)


def record_call(payload: CallRecordRequest) -> CallRecordResponse:
    calls = load_calls()

    calls.append(payload.dict())

    save_calls(calls)

    return CallRecordResponse(status="ok")
