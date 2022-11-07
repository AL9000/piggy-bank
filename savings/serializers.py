from rest_framework import serializers

from savings.models import PiggyBank


class TotalEuroField(serializers.CharField):
    def to_representation(self, value):
        return f'{value / 100:.2f} €'


class PiggyBankSavingsSerializer(serializers.ModelSerializer):
    total_savings = TotalEuroField()

    class Meta:
        model = PiggyBank
        fields = ["total_savings"]


class PiggyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiggyBank
        fields = [
            "cent_one",
            "cent_two",
            "cent_five",
            "cent_ten",
            "cent_twenty",
            "cent_fifty",
            "euro_one",
            "euro_two",
            "euro_five",
            "euro_ten",
            "euro_twenty",
            "euro_fifty",
            "euro_hundred",
            "euro_two_hundred",
            "euro_five_hundred",
        ]
