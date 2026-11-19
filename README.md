# Frappe E-Way Bill Multi-Vehicle Transshipment & FASTag Toll Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![E-Way Bill](https://img.shields.io/badge/GST-E--Way%20Bill%20Rules-emerald.svg)]()
[![FASTag RFID](https://img.shields.io/badge/RFID-FASTag%20Toll%20Sync-orange.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Under Indian Goods and Services Tax transport regulations:
1. Every consignment over ₹50,000 moving inter-state requires an active **E-Way Bill (EWB)**.
2. **Vehicle Breakdown & Transshipment Risk:** During long-haul transport, vehicle breakdowns or hub-and-spoke multi-vehicle transshipments require updating **Part-B (Vehicle Number)** before the goods move onto the new truck.
3. **Section 129 Vehicle Detention Penalties:** If state GST flying squads intercept a truck whose physical vehicle number does not match Part-B, authorities impound the vehicle and impose a punitive **200% penalty on tax payable**.

This Frappe application provides an automated fleet transshipment engine that updates Part-B in real time and reconciles vehicle progress via RFID FASTag toll plaza webhooks.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["ERPNext Delivery Note Dispatched"] -->|Generate Initial E-Way Bill| B["Active EWB (Part-A & Part-B)"]
    B -->|Long-Haul Highway Transit| C["FASTag Toll Plaza RFID Pings"]
    C -->|Detect Vehicle Breakdown / Hub Transshipment| D["Transshipment Event Triggered"]
    D -->|Assign New Relief Truck| E["Automated Part-B Update Controller"]
    E -->|Verify Transit Distance & Validity Extension| F{"EWB Still Valid?"}
    F -->|Within Validity Window| G["API Update to NIC E-Way Bill Portal"]
    F -->|Validity Expired| H["Request Automated Validity Extension"]
    G & H --> I["Generate Updated EWB with New Vehicle Number"]
    I --> J["Sec 129 Interception Shield: Zero Penalty Gate Clearance"]
```

---

## 🚀 Key Engineering Capabilities

- **Instant Multi-Vehicle Part-B Updates:** Programmatically switches transport vehicles during hub-and-spoke transfers.
- **Section 129 Penalty Protection:** Enforces digital locks ensuring no cargo vehicle departs transshipment yards without updated EWB documents.
- **Validity Distance Extension:** Calculates remaining distance and triggers validity extensions when vehicles face highway breakdowns.
- **FASTag Toll Geo-Verification:** Correlates toll plaza transaction timestamps with driver logbook entries.

---

## 📂 Frappe DocType Schema & Data Structure

```text
ewaybill_transshipment/
├── ewaybill_transshipment_core/
│   ├── doctype/
│   │   ├── eway_bill_transit/
│   │   │   ├── eway_bill_transit.json
│   │   │   ├── eway_bill_transit.py
│   │   │   └── eway_bill_transit.js
│   │   └── transshipment_event/
│   │       └── transshipment_event.json
│   └── workspace/
│       └── ewaybill_transshipment_workspace/
│           └── ewaybill_transshipment_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/ewaybill_transshipment.api.execute_multimodal_transshipment`
- **Whitelisted Method:** `@frappe.whitelist() def register_eway_bill(ewb_number, from_pincode, to_pincode, vehicle_number)`
- **Hooks Event:** `on_submit` of `Delivery Note` triggers automated E-Way Bill creation.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/frappe-ewaybill-multimodal-transshipment
bench --site erp.yourdomain.com install-app ewaybill_transshipment
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Engineered for Logistics Transporters, 3PL Fleet Carriers, and Manufacturing Consignors.
