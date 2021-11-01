from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# id, password 자동생성
# 가입자/동아리운영자 구분
class User(AbstractUser):  # ABSTRACT USER
    is_club_admin = models.BooleanField(default=False, help_text="일반 사용자, 동아리 운영자를 구분")

