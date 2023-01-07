from django.urls import path
from . import views
urlpatterns = [
    path("registerdj/", views.signup_django),
]
