from django.urls import path

from savings.views import ShakePiggyBank

urlpatterns = [
    path("shake/", ShakePiggyBank.as_view(), name="shake-piggybank"),
]
