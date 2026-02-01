import json
from pathlib import Path
from api.models import MetricsSummaryResponse

CALLS_FILE = Path("api/data/calls.json")


def load_calls():
    if not CALLS_FILE.exists():
        return []
    with open(CALLS_FILE) as f:
        return json.load(f)


def get_metrics_summary() -> MetricsSummaryResponse:
    calls = load_calls()

    total_calls = len(calls)

    booked = [c for c in calls if c["outcome"] == "booked"]
    transferred = [c for c in calls if c["outcome"] == "transferred"]
    no_match = [c for c in calls if c["outcome"] == "no_match"]
    rejected = [c for c in calls if c["outcome"] == "rejected"]

    booking_rate = len(booked) / total_calls if total_calls else 0

    avg_rate = (
        sum(c["final_rate"] for c in booked if c.get("final_rate") is not None) / len(booked)
        if booked else 0
    )

    avg_rounds = (
        sum(c["negotiation_rounds"] for c in calls) / total_calls
        if total_calls else 0
    )

    sentiment_breakdown = {
        "positive": sum(1 for c in calls if c["sentiment"] == "positive"),
        "neutral": sum(1 for c in calls if c["sentiment"] == "neutral"),
        "negative": sum(1 for c in calls if c["sentiment"] == "negative"),
    }

    return MetricsSummaryResponse(
        total_calls=total_calls,
        booked_calls=len(booked),
        transferred_calls=len(transferred),
        no_match_calls=len(no_match),
        rejected_calls=len(rejected),
        booking_rate=round(booking_rate, 2),
        average_final_rate=round(avg_rate, 2),
        average_negotiation_rounds=round(avg_rounds, 2),
        sentiment_breakdown=sentiment_breakdown
    )
