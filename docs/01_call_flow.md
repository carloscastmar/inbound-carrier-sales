 # Inbound Carrier Call Flow

This document describes the end-to-end flow for inbound carrier calls handled by the AI agent prior to escalation to a human broker.

## High-Level Call Flow

![AI Agent Call Flow](./images/ai_agent_call_flow.png)

## Flow Description

The AI agent handles the full automated portion of the inbound carrier call.

1. The call begins with carrier authentication using the MC number and FMCSA verification.
2. Once authenticated, the agent collects lane and availability preferences from the carrier.
3. The system searches for matching loads based on those preferences.
4. If no matching loads are found, the agent asks for clarification once and retries the search.
5. If a suitable load is found, the agent pitches the load details and negotiates pricing with up to three back-and-forth attempts.
6. If a price is agreed, or if no suitable load is found after clarification, the call is escalated to a human broker.
7. After the AI interaction ends, structured data is extracted and the call is classified by outcome and carrier sentiment.

All extraction and classification is scoped strictly to the AI-handled portion of the call.
