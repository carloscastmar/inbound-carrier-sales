# Negotiation Logic

Rate negotiation is handled using HappyRobot’s native negotiation capabilities to keep the conversation natural and responsive.

The client system provides pricing boundaries and constraints through a dedicated API endpoint. These constraints are fetched once per call and used to guide the negotiation.

This approach avoids unnecessary API calls during the conversation while ensuring all pricing decisions remain within defined business limits.