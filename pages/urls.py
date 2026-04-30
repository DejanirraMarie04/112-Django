from django.urls import path
from .views import (
    AboutPageView,
    HomePageView,
    contact_me,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", contact_me, name="contact"),
]