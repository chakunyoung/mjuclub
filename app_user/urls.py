from django.urls import path
from . import views


# url에서 사용할때 "user:path/" 로 사용
app_name = "user"


urlpatterns = [

    # 유저 페이지
    path('', views.user, name="user"),  # url경로, views.py 함수명, html name
    # path가 '' 이므로 
    # 127.0.0.1:8000/user 그대로

    # 유저 정보
    path('user_info/', views.user_info, name="user_info"),     # url경로, views.py 함수명, html name
    # path가 'userInfo' 이므로 
    # 127.0.0.1:8000/user/userInfo

    # 유저 로그인
    path('user_login/', views.user_login, name="user_login"),

    # 유저 회원가입
    path('user_signup/', views.user_signup, name="user_signup"),

    # 유저 로그아웃
    path('user_logout/', views.user_logout, name="user_logout"),

]