# Metrics and Reporting

This document describes how use case metrics are captured and reported for the inbound carrier sales automation demo.

The goal of the metrics layer is to provide visibility into system performance without relying on platform-native analytics.

---

## Metrics Strategy

Metrics are derived from call outcomes recorded by the system after each inbound interaction.

Instead of tracking low-level conversational events, the system focuses on **business-relevant outcomes**, such as bookings, negotiation behavior, and carrier sentiment.

This approach mirrors how real brokerage teams evaluate automation success.

---

## Captured Metrics

The system exposes a summary report with the following metrics:

### Volume Metrics
- **total_calls**  
  Total number of inbound carrier calls handled.

- **booked_calls**  
  Number of calls resulting in a successfully booked load.

- **transferred_calls**  
  Calls escalated to a human broker.

- **no_match_calls**  
  Calls where no suitable load was found.

- **rejected_calls**  
  Calls where the carrier declined the offered load.

---

### Performance Metrics
- **booking_rate**  
  Percentage of calls that resulted in a booking.

- **average_final_rate**  
  Average agreed rate for booked loads.

- **average_difference**  
  Average difference between the final rate and the initial rate of the load.

- **average_negotiation_rounds**  
  Average number of negotiation turns per call.

---

### Sentiment Metrics
- **sentiment_breakdown**  
  Distribution of carrier sentiment (positive, neutral, negative) based on the AI-handled portion of the call.

---

## Reporting Mechanism

Metrics are exposed through a dedicated API endpoint that aggregates call records into a single summary response.

This endpoint can be consumed by:
- A custom dashboard
- A BI or analytics tool
- Operational reporting workflows

For the demo, metrics are presented directly via the API to emphasize product behavior and system design rather than visualization tooling.
