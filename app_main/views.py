from django.shortcuts import render, get_object_or_404
from app_club.models import Club, PostScript


def main(req):
    clubs = Club.objects.all()
    club3 = Club.objects.all().order_by('-club_admin_id')[:3]
    return render(req, 'main.html', {'clubs': clubs, "club3": club3})


# 테스트
def test(req):
    return render(req, 'maintest.html')


