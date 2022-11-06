from django.urls import path

from savings.views import PiggyBankAPIView

urlpatterns = [
    path("", PiggyBankAPIView.as_view(), name="piggy-bank"),
]
