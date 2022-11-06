from rest_framework import serializers

from savings.models import PiggyBank


class PiggyBankSavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiggyBank
        fields = ["savings"]
