from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_424_FAILED_DEPENDENCY


class PiggyBankDoesNotExists(APIException):
    status_code = HTTP_424_FAILED_DEPENDENCY
    default_detail = "You don't have your own piggy bank yet! Make some savings first."
    default_code = "piggybank_does_not_exists"
