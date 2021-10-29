from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# id, password 자동생성
# 가입자/동아리운영자 구분,
class User(AbstractUser):  # ABSTRACTUSER
    is_club_admin = models.BooleanField(default=False)

