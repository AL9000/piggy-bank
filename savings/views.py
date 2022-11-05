from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from savings.models import PiggyBank


SHAKING_ERROR_MSG = (
    "You don't have any savings yet! Make some before you shake your piggy bank again."
)


class ShakePiggyBank(APIView):
    """
    Returns your savings amount from your piggy bank, or an error if you haven't done
    any savings yet.
    """

    def get(self, request):
        try:
            piggybank = PiggyBank.get_solo()
        except IntegrityError:
            # Here we got an IntegrityError because the model does not have any default
            # on its savings field. The result is that django will not be able to create
            # it without any value, as it is required by default.
            return Response(
                SHAKING_ERROR_MSG,
                status=status.HTTP_412_PRECONDITION_FAILED,
            )
        return Response(piggybank.savings)
