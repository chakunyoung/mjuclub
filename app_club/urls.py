from django.urls import path
from . import views

app_name = "club"

urlpatterns = [
    # 동아리 메인화면
    path('', views.club, name="club"),

    # 동아리 등록화면
    path('signup/', views.club_signup, name="club_signup"),

    # 동아리 수정화면
    path('update/<str:name>/', views.club_update, name='club_update'),

    # 동아리 세부정보
    path('info/<str:name>/', views.club_info, name='club_info'),

    # 동아리 이름 , session.user 로 작성
    # 오류였던것 - url patterns 가 위와 겹쳐서 여기를 인식못했음
    path('info1/<str:name>/', views.club_post, name='club_post'),

]