from django.urls import path

from savings.views import MakeSavings, ShakePiggyBank

urlpatterns = [
    path("shake/", ShakePiggyBank.as_view(), name="shake-piggybank"),
    path("make-savings/", MakeSavings.as_view(), name="make-savings"),
]
