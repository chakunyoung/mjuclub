from django.urls import path
from . import views


app_name = "user"


urlpatterns = [

    path('', views.user, name="user"),  # url경로, views.py 함수명, html name
    # path가 '' 이므로 
    # 127.0.0.1:8000/user 그대로

    path('userInfo/', views.userInfo, name="userInfo"),     # url경로, views.py 함수명, html name
    # path가 'userInfo' 이므로 
    # 127.0.0.1:8000/user/userInfo

    path('user_login/', views.user_login, name="user_login"),




]