from rest_framework import serializers

from savings.models import PiggyBank


class PiggyBankSavingsSerializer(serializers.ModelSerializer):
    total_savings = serializers.SerializerMethodField()

    class Meta:
        model = PiggyBank
        fields = ["total_savings"]

    def get_total_savings(self, obj):
        total_savings = 0
        for key, value in PiggyBank.CENTS_TO_EUROS.items():
            total_savings += getattr(obj, key) * value
        return f"{total_savings / 100:.2f} €"


class PiggyBankFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiggyBank
        exclude = ["id"]

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            # add all new coins and banknotes to the existing ones in the piggy bank
            setattr(instance, key, getattr(instance, key) + value)
        instance.save()
        return instance
