from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
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
        "euro_one_hundred": 10_000,
        "euro_two_hundred": 20_000,
        "euro_five_hundred": 50_000,
    }

    cent_one = models.PositiveIntegerField(
        _("one cent"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_two = models.PositiveIntegerField(
        _("two cent"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_five = models.PositiveIntegerField(
        _("five cent"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_ten = models.PositiveIntegerField(
        _("ten cent"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_twenty = models.PositiveIntegerField(
        _("twenty cent"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    cent_fifty = models.PositiveIntegerField(
        _("fifty cent"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_one = models.PositiveIntegerField(
        _("one euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_two = models.PositiveIntegerField(
        _("two euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_five = models.PositiveIntegerField(
        _("five euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_ten = models.PositiveIntegerField(
        _("ten euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_twenty = models.PositiveIntegerField(
        _("twenty euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_fifty = models.PositiveIntegerField(
        _("fifty euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_one_hundred = models.PositiveIntegerField(
        _("one hundred euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_two_hundred = models.PositiveIntegerField(
        _("two hundred euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )
    euro_five_hundred = models.PositiveIntegerField(
        _("five hundred euro"), default=0, blank=True, validators=[MinValueValidator(0)]
    )

    total_savings = models.PositiveIntegerField(_(""), default=0)

    class Meta:
        verbose_name = _("Piggy bank")
        # there is only one piggy bank instance at any time
        verbose_name_plural = _("Piggy bank")

    def save(self, *args, **kwargs):
        self.total_savings = 0
        for key, value in self.CENTS_TO_EUROS.items():
            self.total_savings += getattr(self, key) * value
        super().save(*args, **kwargs)
