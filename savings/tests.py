from django.shortcuts import resolve_url
from rest_framework.exceptions import ErrorDetail
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from savings.models import PiggyBank
from savings.serializers import PiggyBankFullSerializer


class PyggyBankShakingTestCase(APITestCase):
    def test_shake_empty_piggybank_must_returns_zero(self):
        url = resolve_url("piggy-bank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["total_savings"], "0.00 €")

    def test_shake_piggybank_must_returns_its_savings_amount(self):
        euro_one_nb = 1  # save 1 euro
        PiggyBank.objects.create(euro_one=euro_one_nb)
        url = resolve_url("piggy-bank")
        response = self.client.get(url)
        self.assertEqual(response.data["total_savings"], "1.00 €")


class PyggyBankMakingSavingsTestCase(APITestCase):
    def test_saving_money_for_the_first_time(self):
        """You must save at least 0.01€, as it is the smallest coin that exists."""
        url = resolve_url("piggy-bank")
        data = {"cent_one": 1}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        piggybank = PiggyBank.get_solo()
        self.assertEqual(piggybank.cent_one, data["cent_one"])

    def test_saving_money_on_a_existing_piggy_bank(self):
        euro_twenty_initial_nb = 10
        PiggyBank.objects.create(euro_twenty=euro_twenty_initial_nb)
        url = resolve_url("piggy-bank")
        data = {"euro_twenty": 32}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)
        piggybank = PiggyBank.get_solo()
        final_euro_twenty_nb = euro_twenty_initial_nb + data["euro_twenty"]
        self.assertEqual(piggybank.euro_twenty, final_euro_twenty_nb)

    def test_saving_amount_cant_be_negative(self):
        """You are not able to save a negative amount of any coin or banknote."""
        url = resolve_url("piggy-bank")
        response = self.client.put(url, {"euro_twenty": -42})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data,
            {
                "euro_twenty": [
                    ErrorDetail(
                        string='Ensure this value is greater than or equal to 0.',
                        code='min_value',
                    )
                ]
            },
        )


class BreakPyggyBankTestCase(APITestCase):
    def test_breaking_the_piggybank_must_reset_every_fields_to_zero(self):
        piggy_bank = PiggyBank.get_solo()
        piggy_bank.euro_one = 2
        piggy_bank.save()
        url = resolve_url("piggy-bank")
        response = self.client.get(url)
        self.assertEqual(response.data["total_savings"], "2.00 €")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        response = self.client.get(url)
        self.assertEqual(response.data["total_savings"], "0.00 €")
        piggy_bank.refresh_from_db()
        # test that all field names that begin by 'euro' or 'cent' are reset to 0
        for field in PiggyBank._meta.get_fields():
            if field.name[:4] in ["euro", "cent"]:
                self.assertEqual(getattr(piggy_bank, field.name), 0)

    def test_breaking_the_piggybank_must_give_back_all_the_savings(self):
        """You are not able to save a negative amount of any coin or banknote."""
        piggy_bank = PiggyBank.get_solo()
        piggy_bank.euro_one = 2
        piggy_bank.euro_five = 8
        piggy_bank.cent_five = 14
        piggy_bank.save()
        serializer = PiggyBankFullSerializer(instance=piggy_bank)
        url = resolve_url("piggy-bank")
        response = self.client.get(url)
        self.assertEqual(response.data["total_savings"], "42.70 €")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, serializer.data)
