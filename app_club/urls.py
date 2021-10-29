from django.urls import path
from . import views

app_name = "club"

urlpatterns = [
    path('', views.club, name="club"),



]