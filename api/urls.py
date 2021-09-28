from django.urls import path, include
from products.api.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"category",CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("accounts/", include("accounts.api.urls")),
    path("products/", include("products.api.urls")),
    path("payments/", include("payments.urls")),
    path("subscribers/", include("newsletter.api.urls")),
]
