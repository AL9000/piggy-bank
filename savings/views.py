from django.db import IntegrityError
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from savings.exceptions import PiggyBankDoesNotExists
from savings.models import PiggyBank
from savings.serializers import PiggyBankSavingsSerializer


class PiggyBankAPIView(RetrieveUpdateDestroyAPIView):
    """Handle your own unique piggy bank.

    Do a GET request to "shake" your piggy bank, it will return your savings amount,
    or an error if you haven't done any savings yet.

    Do a PUT request to save some money, just give a strictly positive integer in the
    'savings' value ; { 'savings': 4000 }

    Do a DELETE request to definitely break your piggy bank and get your money back.
    You will have to save some money again to create a new piggy bank.
    """
    serializer_class = PiggyBankSavingsSerializer

    def get_object(self):
        try:
            return PiggyBank.get_solo()
        except IntegrityError:
            # Here we got an IntegrityError because the model does not have any default
            # on its savings field. The result is that django will not be able to create
            # it without any value, as it is required by default.
            raise PiggyBankDoesNotExists

    def update(self, request, *args, **kwargs):
        serializer = PiggyBankSavingsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            savings = serializer.validated_data.get("savings")
            try:
                piggybank = self.get_object()
            except PiggyBankDoesNotExists:
                PiggyBank.objects.create(savings=savings)
            else:
                piggybank.savings += savings
                piggybank.save()
        return Response(serializer.data)
