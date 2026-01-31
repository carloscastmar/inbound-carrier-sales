# Notes
## Decisions
### Decide between store the data in a db or json


## Reasoning
While HappyRobot workflows are capable of handling much of the logic, I intentionally externalized carrier verification, load matching, and metrics into a separate API. This mirrors a real freight brokerage environment, where core business logic and data ownership live outside the conversational layer. This approach improves testability, portability, and long-term scalability.

## Platform Integration
HappyRobot is used as the conversational and orchestration layer for inbound carrier calls, handling dialog flow, negotiation turns, and call routing.
Core business logic such as carrier verification via the FMCSA API, load search, offer evaluation, and metrics aggregation is implemented in an external service. This mirrors a real freight brokerage architecture where the voice layer interacts with existing internal systems.

## Questions
- Do I need to find a load based on what the client is saying?
- Will the client ask for a specific load?

## How to get a load:
1. Specific load provided -> Retrieve by ID -> Pitch details
2. Preferences provided -> Search matching loads -> Rank by relevance -> Pitch top result
3. No matches found -> Ask one clarifying question (e.g. rate flexibility or date range) -> Re-run search once -> If still no match → fallback
4. No preferences provided -> Pitch earliest pickup load as default