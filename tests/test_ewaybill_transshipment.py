import unittest
from ewaybill_transshipment.engine import EWayBillRecord, EWayBillTransshipmentEngine

class TestEWayBillTransshipmentEngine(unittest.TestCase):
    def setUp(self):
        self.engine = EWayBillTransshipmentEngine("TRANS-GATI-0012")

    def test_transshipment_part_b(self):
        ewb = EWayBillRecord(
            ewb_number="EWB-2026-99120412", from_pincode="110001", to_pincode="400001",
            approximate_distance_km=1400, current_vehicle_number="DL-01-AB-1234",
            valid_until_datetime="2026-03-20T23:59:59"
        )
        self.engine.register_eway_bill(ewb)

        res = self.engine.execute_multimodal_transshipment("EWB-2026-99120412", "MH-04-CD-5678", "452001", "BREAKDOWN_NEAR_INDORE")
        self.assertTrue(res["part_b_updated"])
        self.assertEqual(res["new_assigned_vehicle"], "MH-04-CD-5678")
        self.assertTrue(res["sec_129_detention_penalty_safeguarded"])

if __name__ == "__main__":
    unittest.main()
