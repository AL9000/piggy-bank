from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from savings.models import PiggyBank
from savings.serializers import PiggyBankSavingsSerializer, PiggyBankFullSerializer


class PiggyBankAPIView(RetrieveUpdateDestroyAPIView):
    """Handle your own unique piggy bank.

    Do a GET request to "shake" your piggy bank, it will return your savings amount,
    in euros.

    Do a PUT request to save some money, just give a positive integer in one of the
    following values representing the number of each coin or banknote you are putting
    in the piggy bank : cent_one, cent_two, cent_five, cent_ten, cent_twenty,
    cent_fifty, euro_one, euro_two, euro_five, euro_ten, euro_twenty, euro_fifty,
    euro_hundred, euro_two_hundred, euro_five_hundred

    Do a DELETE request to definitely break your piggy bank and get your money back.
    It will return all the coins and banknotes you had put inside.
    """

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PiggyBankSavingsSerializer
        return PiggyBankFullSerializer

    def get_object(self):
        return PiggyBank.get_solo()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        self.perform_destroy(instance)
        return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
