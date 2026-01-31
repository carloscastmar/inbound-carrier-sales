# Load Search and Selection Logic

This document describes how inbound carrier requests are mapped to available loads.

## Inputs
A carrier may provide:
- A specific load ID
- Preferences (origin, destination, pickup window, equipment, rate)
- No specific information

## Decision Flow

### 1. Specific Load Requested
If a valid load ID is provided:
- Retrieve the load directly
- Pitch load details to the carrier

### 2. Preference-Based Search
If preferences are provided:
- Search available loads matching the criteria
- Rank results based on relevance
- Pitch the highest-ranked load

### 3. No Matching Loads
If no loads match the provided preferences:
- The assistant attempts one clarification (e.g., date or rate flexibility)
- If no suitable match is found, the system falls back to a default load

### 4. No Preferences Provided
If the carrier provides no preferences:
- The system selects the load with the earliest pickup date
- This ensures forward progress and avoids dead-end calls

## Rationale
This approach balances realism and simplicity while ensuring that every inbound call can progress to a meaningful outcome during the demo.

## Production Considerations
In a production environment, load ranking could incorporate:
- Margin optimization
- Carrier historical performance
- Lane density
