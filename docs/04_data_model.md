# Data Model

This document describes the core data structures used in the inbound carrier sales automation demo.

For simplicity and transparency, all data is stored in static JSON files. This approach allows the system behavior to be easily inspected during the demo while still closely mirroring how real brokerage systems structure and consume data.

---

## Load Model

Loads represent freight opportunities available to be booked by carriers. In a production environment, this data would typically come from a Transportation Management System (TMS) or load board integration.

Each load contains the following fields:

- **load_id**  
  Unique identifier for the load.

- **origin**  
  Starting location (city, state).

- **destination**  
  Delivery location (city, state).

- **pickup_datetime**  
  Date and time when the load is available for pickup.

- **delivery_datetime**  
  Expected delivery date and time.

- **equipment_type**  
  Type of equipment required (e.g. Dry Van, Reefer, Flatbed).

- **loadboard_rate**  
  Listed rate for the load before negotiation.

- **notes**  
  Additional operational details relevant to the carrier (e.g. temperature requirements, appointment type).

- **weight**  
  Total load weight in pounds.

- **commodity_type**  
  Type of goods being transported.

- **num_of_pieces**  
  Number of pallets or pieces.

- **miles**  
  Estimated distance for the lane.

- **dimensions**  
  Description of cargo dimensions or packaging.

Loads are stored in a JSON file and queried by the load search service during inbound calls.

---

## Call Record Model

Call records represent the outcome of inbound carrier interactions handled by the AI agent.

Each call record includes:

- **call_id**  
  Unique identifier for the call.

- **carrier_mc**  
  MC number provided by the carrier.

- **load_id**  
  Load discussed during the call (if applicable).

- **final_rate**  
  Agreed rate if the load was booked.

- **negotiation_rounds**  
  Number of negotiation turns before resolution.

- **outcome**  
  Final call outcome (booked, no_match, rejected, transferred).

- **sentiment**  
  Sentiment classification of the carrier during the AI-handled portion of the call.

- **timestamp**  
  Time when the call ended.

Call records are appended to a JSON file and serve as the source of truth for metrics and reporting.
