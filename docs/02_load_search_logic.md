# Load Search and Selection Logic

This document explains how the system chooses which load to present to a carrier during an inbound call.

The flow described here corresponds to the “Search for loads” step in the inbound call flow diagram (`01_call_flow.md`).

---

## What the Carrier Provides

During the call, the carrier shares some basic details about what they are looking for, such as:

- Where they want to pick up
- Where they want to deliver
- When they are available to pick up
- The type of equipment they have
- Any rate expectations

These details are used to look for suitable loads.

---

## How Loads Are Selected

### 1. Searching Based on Preferences

Once the carrier’s preferences are collected:

- The system looks for loads that match those details.
- The results are ordered so the most relevant option comes first.
- The best matching load is presented to the carrier.

If more than one load looks like a good fit, simple tie-breakers are used, such as:
- Which load picks up sooner
- Which option is easier to explain and negotiate

To keep the conversation focused, only one load is discussed at a time.

---

### 2. When No Loads Are Found

If no loads match the initial preferences:

- The assistant asks one follow-up question to clarify, for example:
  - Whether the pickup time is flexible
  - Whether the rate can be adjusted
- The system searches again using the updated information.

If there are still no suitable loads:
- The assistant does not pitch an unrelated load.
- The call is handed off to a human broker who can assist manually.

This approach avoids wasting the carrier’s time and reflects how real brokerage teams operate.

---

## Why This Approach Was Chosen

The goal is to keep the interaction realistic while making sure every call leads to a reasonable outcome.

By limiting follow-up questions and avoiding forced matches, the system stays helpful without becoming frustrating or overly complex.

---

## Looking Ahead

In a real production system, the load selection process could be improved with additional context, such as:

- Which loads are more profitable
- A carrier’s past lanes or preferences
- Current market conditions

These ideas were intentionally left out of the demo to keep the solution simple and easy to understand.
