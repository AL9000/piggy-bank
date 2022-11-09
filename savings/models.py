from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class PositiveIntegerValidatorField(models.PositiveIntegerField):
    default_validators = [MinValueValidator(0)]


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

    cent_one = PositiveIntegerValidatorField(_("one cent"), default=0, blank=True)
    cent_two = PositiveIntegerValidatorField(_("two cents"), default=0, blank=True)
    cent_five = PositiveIntegerValidatorField(_("five cents"), default=0, blank=True)
    cent_ten = PositiveIntegerValidatorField(_("ten cents"), default=0, blank=True)
    cent_twenty = PositiveIntegerValidatorField(_("twenty cents"), default=0, blank=True)
    cent_fifty = PositiveIntegerValidatorField(_("fifty cents"), default=0, blank=True)
    euro_one = PositiveIntegerValidatorField(_("one euro"), default=0, blank=True)
    euro_two = PositiveIntegerValidatorField(_("two euros"), default=0, blank=True)
    euro_five = PositiveIntegerValidatorField(_("five euros"), default=0, blank=True)
    euro_ten = PositiveIntegerValidatorField(_("ten euros"), default=0, blank=True)
    euro_twenty = PositiveIntegerValidatorField(_("twenty euros"), default=0, blank=True)
    euro_fifty = PositiveIntegerValidatorField(_("fifty euros"), default=0, blank=True)
    euro_one_hundred = PositiveIntegerValidatorField(_("one hundred euros"), default=0, blank=True)
    euro_two_hundred = PositiveIntegerValidatorField(_("two hundred euros"), default=0, blank=True)
    euro_five_hundred = PositiveIntegerValidatorField(_("five hundred euros"), default=0, blank=True)

    class Meta:
        verbose_name = _("Piggy bank")
        # there is only one piggy bank instance at any time
        verbose_name_plural = _("Piggy bank")
