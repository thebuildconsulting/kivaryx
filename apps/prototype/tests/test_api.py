"""Run with `python -m unittest discover -s tests -v` after installing requirements+httpx."""
import os
import tempfile
import unittest
from pathlib import Path

# Must be set before importing the app, which initialises the synthetic database.
TMP = tempfile.TemporaryDirectory(prefix="kivaryx_test_")
os.environ["KIVARYX_DB"] = str(Path(TMP.name) / "test.sqlite3")
from fastapi.testclient import TestClient
from app.main import app


class SyntheticPaymentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.c = TestClient(app)

    @classmethod
    def tearDownClass(cls): cls.c.close();TMP.cleanup()

    def test_dashboard_seeded(self):
        r=self.c.get("/api/dashboard")
        self.assertEqual(r.status_code,200)
        self.assertTrue(r.json()["synthetic"])
        self.assertGreater(r.json()["total"],10)

    def test_payment_and_same_key_replay(self):
        data={"merchant_id":"mrc_meridian","amount_minor":2500,"currency":"GBP", "idempotency_key":"unit-test-1"}
        r=self.c.post("/api/payments",json=data)
        self.assertEqual(r.status_code,200,r.text)
        tx=r.json()["transaction"]
        self.assertEqual(tx["status"],"approved")
        self.assertEqual(tx["model_version"],"risk-simulator-rules-v0.1")
        r2=self.c.post("/api/payments",json=data)
        self.assertTrue(r2.json()["replayed"])
        self.assertEqual(r2.json()["transaction"]["transaction_id"],tx["transaction_id"])
        detail=self.c.get("/api/payments/"+tx["transaction_id"]).json()
        self.assertEqual(len(detail["events"]),3)

    def test_key_conflict(self):
        data={"merchant_id":"mrc_meridian","amount_minor":2500,"currency":"GBP", "idempotency_key":"unit-test-conflict"}
        self.assertEqual(self.c.post("/api/payments",json=data).status_code,200)
        data["amount_minor"]=2600
        self.assertEqual(self.c.post("/api/payments",json=data).status_code,409)

    def test_high_value_review(self):
        r=self.c.post("/api/payments",json={"merchant_id":"mrc_lumina","amount_minor":220000,"idempotency_key":"unit-test-risk"})
        self.assertEqual(r.json()["transaction"]["status"],"requires_review")

    def test_no_sensitive_fields(self):
        rows=self.c.get("/api/payments").json()["items"]
        for row in rows:
            self.assertNotIn("card_number",row)
            self.assertNotIn("cvv",row)
            self.assertNotIn("payload_hash",row)


if __name__=="__main__":unittest.main()
