from django.urls import path
from . import views

app_name = "match"

urlpatterns = [
    path('', views.match, name="match"),

    path('match_result', views.match_result, name="match_result"),


]

