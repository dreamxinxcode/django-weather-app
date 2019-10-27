from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("", views.homepage_view, name="homepage_view"),
    path("about/", views.about_view, name="about_view"),
    path("contact/", views.contact_view, name="contact_view"),   
]
