from django.shortcuts import resolve_url
from rest_framework.exceptions import ErrorDetail
from rest_framework.test import APITestCase

from savings.models import PiggyBank
from savings.exceptions import PiggyBankDoesNotExists


class PyggyBankShakingTestCase(APITestCase):
    def test_shake_piggybank_must_returns_an_error_if_the_piggybank_was_not_created_before(self):
        url = resolve_url("piggy-bank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, PiggyBankDoesNotExists.status_code)
        self.assertEqual(response.data["detail"], PiggyBankDoesNotExists.default_detail)

    def test_shake_piggybank_must_returns_its_savings_amount(self):
        saving_amount = 2000
        PiggyBank.objects.create(savings=saving_amount)  # 2000 euro cents = 20€
        url = resolve_url("piggy-bank")
        response = self.client.get(url)
        self.assertEqual(response.data["savings"], saving_amount)


class PyggyBankMakingSavingsTestCase(APITestCase):
    def test_saving_money_for_the_first_time(self):
        """You must save at least 0.01€, as it is the smallest coin that exists."""
        url = resolve_url("piggy-bank")
        saving_amount = 1
        response = self.client.put(url, {"savings": saving_amount})
        self.assertEqual(response.status_code, 200)
        piggybank = PiggyBank.get_solo()
        self.assertEqual(piggybank.savings, saving_amount)

    def test_saving_money_on_a_existing_piggy_bank(self):
        initial_savings = 123456789
        PiggyBank.objects.create(savings=initial_savings)
        url = resolve_url("piggy-bank")
        saving_amount = 987654321
        response = self.client.put(url, {"savings": saving_amount})
        self.assertEqual(response.status_code, 200)
        piggybank = PiggyBank.get_solo()
        self.assertEqual(piggybank.savings, initial_savings + saving_amount)

    def test_saving_amount_cant_be_zero(self):
        """You are not able to save 0 euros, or even save a negative amount."""
        url = resolve_url("piggy-bank")
        response = self.client.put(url, {"savings": 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data,
            {
                "savings": [
                    ErrorDetail(
                        string='Ensure this value is greater than or equal to 1.',
                        code='min_value',
                    )
                ]
            },
        )

    def test_saving_amount_cant_be_negative(self):
        """You are not able to save 0 euros, or even save a negative amount."""
        url = resolve_url("piggy-bank")
        response = self.client.put(url, {"savings": -42})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data,
            {
                "savings": [
                    ErrorDetail(
                        string='Ensure this value is greater than or equal to 1.',
                        code='min_value',
                    )
                ]
            },
        )
