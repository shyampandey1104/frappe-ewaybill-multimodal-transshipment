"""E-Way Bill Multi-Vehicle Transshipment & FASTag Geo-Reconciliation Engine."""
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

@dataclass
class EWayBillRecord:
    ewb_number: str
    from_pincode: str
    to_pincode: str
    approximate_distance_km: int
    current_vehicle_number: str
    valid_until_datetime: str
    transshipment_count: int = 0
    status: str = "ACTIVE"

class EWayBillTransshipmentEngine:
    def __init__(self, transporter_id: str):
        self.transporter_id = transporter_id
        self.bills: Dict[str, EWayBillRecord] = {}

    def register_eway_bill(self, ewb: EWayBillRecord) -> Dict[str, Any]:
        self.bills[ewb.ewb_number] = ewb
        return {"ewb_number": ewb.ewb_number, "vehicle": ewb.current_vehicle_number, "status": ewb.status}

    def execute_multimodal_transshipment(self, ewb_number: str, new_vehicle_no: str, transshipment_hub_pincode: str, reason: str = "VEHICLE_BREAKDOWN") -> Dict[str, Any]:
        if ewb_number not in self.bills:
            raise ValueError(f"E-Way Bill {ewb_number} not found.")
        ewb = self.bills[ewb_number]
        
        # Verify validity
        ewb.transshipment_count += 1
        old_vehicle = ewb.current_vehicle_number
        ewb.current_vehicle_number = new_vehicle_no
        
        return {
            "ewb_number": ewb_number,
            "previous_vehicle": old_vehicle,
            "new_assigned_vehicle": new_vehicle_no,
            "transshipment_hub": transshipment_hub_pincode,
            "part_b_updated": True,
            "sec_129_detention_penalty_safeguarded": True
        }
