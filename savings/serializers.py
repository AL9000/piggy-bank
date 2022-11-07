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


class PiggyBankFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiggyBank
        exclude = ["id", "total_savings"]
