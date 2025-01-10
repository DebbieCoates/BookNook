from . import views
from django.urls import path, include

urlpatterns = [
     # Link to Homepage
    path('', views.HomePage.as_view(), name='home'),

    #Link to accounts
    path("accounts/", include("allauth.urls")),



]
