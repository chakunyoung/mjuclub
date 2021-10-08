"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app_match import urls as match_urls
from app_user import urls as user_urls
from app_club import urls as club_urls
from app_main import urls as main_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urls)),               # 127.0.0.1:8000/
    path('user/', include(user_urls)),          # 127.0.0.1:8000/user
    path('club/', include(club_urls)),          # 127.0.0.1:8000/club
    path('match/', include(match_urls)),        # 127.0.0.1:8000/match
    # 해당 app의 urls.py로 이동

]
