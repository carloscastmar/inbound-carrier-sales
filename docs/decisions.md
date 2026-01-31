# Design Decisions

This document captures the key design decisions made while building the inbound carrier sales proof of concept, along with the reasoning behind them.

---

## Data Storage Choice

**Decision**  
Use JSON files for load data and call results in the demo.

**Reasoning**  
For the purposes of this take-home assignment, JSON files allow for fast setup, easy inspection, and simple resets during demos. This approach keeps the system lightweight while still behaving similarly to a real load source.

**Production Consideration**  
In a real deployment, this data would live in a database to support concurrent access, better performance, and historical analysis.

---

## System Boundaries and Architecture

**Decision**  
Separate conversational logic from business logic by using an external API.

**Reasoning**  
Although HappyRobot workflows are capable of handling much of the logic, carrier verification, load matching, pricing evaluation, and metrics were intentionally implemented in a separate service. This mirrors how real freight brokerages operate, where core business logic and data ownership live outside the conversational layer.

This separation improves clarity, testability, and makes the solution easier to extend beyond a single voice platform.

---

## Platform Integration

**Decision**  
Use HappyRobot as the orchestration and conversation layer only.

**Details**  
HappyRobot is responsible for:
- Managing the inbound call flow
- Collecting carrier inputs
- Handling negotiation turns
- Routing calls to human brokers when needed

The external API is responsible for:
- Verifying carriers using the FMCSA API
- Searching and ranking loads
- Evaluating counteroffers
- Storing structured call outcomes
- Powering the metrics dashboard

This reflects a realistic customer integration where HappyRobot plugs into existing internal systems.

---

## Load Search Assumptions

**Decision**  
Assume carriers call with general preferences rather than specific load IDs.

**Reasoning**  
In real inbound carrier sales, carriers typically describe their availability and lane preferences instead of referencing internal load identifiers. The system was designed around this behavior to keep interactions realistic and natural.

If no suitable load is found after one clarification attempt, the call is escalated to a human broker rather than forcing an unrelated match.

---

## Data Extraction Scope

**Decision**  
Extract and classify data only from the AI-handled portion of the call.

**Reasoning**  
All structured data extraction, outcome classification, and sentiment analysis are performed before the call is transferred to a human broker. Post-transfer conversations are intentionally excluded, as they are less structured and would typically be handled by separate CRM or call-recording tools in a production environment.

This keeps the automation focused, consistent, and easy to evaluate.
