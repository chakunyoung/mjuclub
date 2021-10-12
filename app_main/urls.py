from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),


    # 테스트
    path('test', views.test, name="test"),

]