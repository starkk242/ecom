from django.urls import include, path
from .views import CustomRegisterView, CustomLoginView

urlpatterns = [
    path("login/", CustomLoginView.as_view()),
    path("register/", CustomRegisterView.as_view()),
]
