from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, PostScript
from django.db.models import Avg, Max, Min, Sum, Count


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


# 동아리 세부 정보, 유저가 작성한 후기 보기
def club_info(req, name):
    if req.method == 'GET':
        club = Club.objects.get(club_name=name)

        # Club.clubname , PostScripts.clubname
        ps = PostScript.objects.filter(club_name__club_name=name)
        return render(req, 'club_info.html', {'club': club, 'ps': ps})

    return render(req, 'club_info.html')


# 동아리 후기 작성
def club_post(req, name):
    if req.method == 'POST':
        club = Club.objects.get(club_name=name)  # path/club_admin get
        post_text = req.POST.get('post_text')
        post_score = req.POST.get('post_score')

        # 동아리 후기 저장
        ps = PostScript(
            club_name=club,  # club admin
            user_name=req.user,  # session user
            post_text=post_text,
            post_score=post_score
        )
        ps.save()
        
        # 동아리 후기들의 평균을 작성된 club_score에 저장
        club_score_avg = PostScript.objects.filter(club_name__club_name=name).aggregate(Avg('post_score'))
        print(club_score_avg['post_score__avg'])
        club.club_score = club_score_avg['post_score__avg']
        # 소수점 이하는 버린채로 save
        club.save()
        return redirect('club:club_info', name)
    #
    return render(req, '')

