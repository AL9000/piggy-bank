from django.db import IntegrityError
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from savings.exceptions import PiggyBankDoesNotExists
from savings.models import PiggyBank
from savings.serializers import PiggyBankSavingsSerializer


class ShakePiggyBank(RetrieveAPIView):
    """Returns your savings amount from your piggy bank, or an error if you haven't done
    any savings yet."""
    serializer_class = PiggyBankSavingsSerializer

    def get_object(self):
        try:
            return PiggyBank.get_solo()
        except IntegrityError:
            # Here we got an IntegrityError because the model does not have any default
            # on its savings field. The result is that django will not be able to create
            # it without any value, as it is required by default.
            raise PiggyBankDoesNotExists


class MakeSavings(UpdateAPIView):
    """Save money into your piggy bank"""
    serializer_class = PiggyBankSavingsSerializer

    def update(self, request, *args, **kwargs):
        serializer = PiggyBankSavingsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            savings = serializer.validated_data.get("savings")
            try:
                piggybank = PiggyBank.get_solo()
            except IntegrityError:
                PiggyBank.objects.create(savings=savings)
            else:
                piggybank.savings += savings
                piggybank.save()
        return Response(serializer.data)
