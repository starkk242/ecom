from django.urls import path

from .views import CreatePaymentLink

urlpatterns = [
        path("", CreatePaymentLink.as_view(), name="charge_view"),
        ]

