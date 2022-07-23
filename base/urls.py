from unicodedata import name
from django.urls import path
from . import views
from .views import contactPage, thanks

urlpatterns = [
    path('', views.homePage, name="index"),
    path('contact/', views.contactPage, name="contact"),
    path('thanks/', thanks, name="thanks"),
]
