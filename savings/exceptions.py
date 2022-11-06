from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_424_FAILED_DEPENDENCY


class PiggyBankDoesNotExists(APIException):
    status_code = HTTP_424_FAILED_DEPENDENCY
    default_detail = (
        "You don't have any savings yet! Make some before shaking your piggy bank "
        "again."
    )
    default_code = "piggybank_does_not_exists"
