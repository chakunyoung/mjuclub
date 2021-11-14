from django.db import models
from app_user import models as user_model
# Create your models here.


# 동아리 (동아리 이름, 동아리 장, 동아리 정보, 동아리 내용, 동아리 위치, 동아리 점수, 동아리 사진)
# 동아리 운영자와 일대일 관계
class Club(models.Model):
    club_name = models.CharField(max_length=20)
    club_admin = models.OneToOneField(
        user_model.User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    club_info = models.CharField(max_length=20)
    club_contents = models.TextField(blank=False, null=False, default="")
    club_loc = models.CharField(max_length=20)
    club_score = models.FloatField(default=0, blank=True)
    club_images = models.ImageField(blank=True, upload_to="images/club", null=True)

    def __str__(self):
        return self.club_name


# 동아리 후기 (동아리 fk, 유저 fk, 후기 내용, 후기 점수)
# 동아리, 유저의 후기는 다대다 관계
class PostScript(models.Model):
    club_name = models.ForeignKey(
        Club,
        on_delete=models.CASCADE
    )
    user_name = models.ForeignKey(
        user_model.User,
        on_delete=models.CASCADE
    )
    post_text = models.TextField(blank=False, null=False, default="")
    post_score = models.FloatField(default=0, blank=True)

    def __str__(self):
        return self.post_text

