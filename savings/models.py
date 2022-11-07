from django.core.validators import MinValueValidator
from django.db import models
from solo.models import SingletonModel


class PiggyBank(SingletonModel):
    CENTS_TO_EUROS = {
        "cent_one": 1,
        "cent_two": 2,
        "cent_five": 5,
        "cent_ten": 10,
        "cent_twenty": 20,
        "cent_fifty": 50,
        "euro_one": 100,
        "euro_two": 200,
        "euro_five": 500,
        "euro_ten": 1_000,
        "euro_twenty": 2_000,
        "euro_fifty": 5_000,
        "euro_hundred": 10_000,
        "euro_two_hundred": 20_000,
        "euro_five_hundred": 50_000,
    }

    cent_one = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_two = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_five = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_ten = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_twenty = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_fifty = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_one = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_two = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_five = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_ten = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_twenty = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_fifty = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_hundred = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_two_hundred = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_five_hundred = models.PositiveIntegerField(
        default=0, blank=True, validators=[MinValueValidator(0)]
    )

    total_savings = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_savings = 0
        for key, value in self.CENTS_TO_EUROS.items():
            self.total_savings += getattr(self, key) * value
        super().save(*args, **kwargs)
