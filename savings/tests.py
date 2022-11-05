from django.shortcuts import resolve_url
from rest_framework.test import APITestCase

from savings.models import PiggyBank
from savings.views import SHAKING_ERROR_MSG


class PyggyBankShakingTestCase(APITestCase):
    def test_shake_piggybank_must_returns_an_error_if_the_piggybank_was_not_created_before(self):
        url = resolve_url("shake-piggybank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 412)
        self.assertEqual(response.data, SHAKING_ERROR_MSG)

    def test_shake_piggybank_must_returns_its_savings_amount(self):
        PiggyBank.objects.create(savings=2000)  # 2000 euro cents = 20€
        url = resolve_url("shake-piggybank")
        response = self.client.get(url)
        self.assertEqual(response.data, 2000)
