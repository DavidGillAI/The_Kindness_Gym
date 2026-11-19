"""Offline regression checks for failures after the daily allowance is reserved."""

import importlib
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from fastapi.testclient import TestClient
from openai import APIError


class FailureMessageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # No real credentials, provider requests or database calls are needed.
        with patch("openai.OpenAI"):
            cls.main = importlib.import_module("mvp.main")
        cls.client = TestClient(cls.main.app)

    def post_with_result(self, *, error=None, result=None):
        with patch.object(self.main, "reserve_usage", return_value="allowed") as reserve:
            with patch.object(self.main.client.responses, "create",
                              side_effect=error, return_value=result):
                response = self.client.post("/coach", data={
                    "dilemma": "A fictional everyday dilemma.", "access_code": "fake-code",
                })
        reserve.assert_called_once_with("fake-code")
        self.assertEqual(response.status_code, 502)
        self.assertIn("used today&#x27;s submission", response.text)
        self.assertIn("midnight in Lisbon", response.text)
        self.assertNotIn("Please try again", response.text)
        self.assertNotIn("so you can try again", response.text)
        self.assertNotIn("fake-code", response.text)

    def test_provider_failure_explains_consumed_allowance(self):
        self.post_with_result(error=APIError("Test failure", request=None, body=None))

    def test_empty_reply_explains_consumed_allowance(self):
        self.post_with_result(result=SimpleNamespace(
            model="fake-model", status="completed", usage=None, output_text="  ",
        ))


if __name__ == "__main__":
    unittest.main()
