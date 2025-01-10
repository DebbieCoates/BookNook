from . import views
from django.urls import path

urlpatterns = [
    # Link to Homepage
    path('', views.HomePage.as_view(), name='home'),

]
