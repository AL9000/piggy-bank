from django.core.validators import MinValueValidator
from django.db import models
from solo.models import SingletonModel


class PiggyBank(SingletonModel):
    savings = models.PositiveIntegerField(validators=[MinValueValidator(1)])
