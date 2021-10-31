from django.shortcuts import render, get_object_or_404, redirect
from .models import Club


# 동아리 메인화면
def club(request):
    clubs = Club.objects.all()
    return render(request, 'club.html', {'clubs': clubs})


# 동아리 등록
def club_signup(req):
    # 동아리 버튼 클릭 시
    if req.method == 'POST':
        club_name = req.POST.get('club_name')
        club_admin = req.user  # 현재 세션 user
        club_info = req.POST.get('club_info')
        club_contents = req.POST.get('club_contents')
        club_loc = req.POST.get('club_loc')
        club_images = images = req.FILES.get('club_images')

        club = Club(club_name=club_name,
                    club_admin=club_admin,
                    club_info=club_info,
                    club_contents=club_contents,
                    club_loc=club_loc,
                    club_images=club_images,
                    )
        club.save()
        return redirect('club:club')
    # 동아리 등록 화면
    return render(req, 'club_signup.html')


# 동아리 정보
def club_info(req, name):
    if req.method == 'GET':
        club = Club.objects.get(club_name=name)
        return render(req, 'club_info.html', {'club': club})

    return render(req, 'club_info.html')

