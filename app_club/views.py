from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, PostScript
from app_user.models import User
from django.db.models import Avg  # Max, Min, Sum, Count


# 동아리 메인화면
def club(req):
    clubs = Club.objects.all()

    # 동아리 운영자 화면
    user = req.user
    if user.is_authenticated:
        if user.is_club_admin == 1:
            # 동아리 운영자이면서 동아리를 이미 생성함.
            if Club.objects.filter(club_admin=user).exists():
                club = Club.objects.get(club_admin=user)
                message = 1
                return render(req, 'club.html', {'clubs': clubs, 'club': club, 'message': message})

            # 동아리 운영자이지만 동아리를 아직 생성하지 않음.
            else:
                message = 0
                return render(req, 'club.html', {'clubs': clubs, 'message': message})

    # 일반유저, 비로그인 유저 화면
    return render(req, 'club.html', {'clubs': clubs})


# 동아리 상세 정보, 유저가 작성한 후기 보기
def club_info(req, name):
    if req.method == 'GET':
        club = Club.objects.get(club_name=name)

        # Club.clubname , PostScripts.clubname
        # 동아리 명을 기준으로 filter
        ps = PostScript.objects.filter(club_name__club_name=name)
        return render(req, 'club_info.html', {'club': club, 'ps': ps})
    #
    return render(req, '')


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


# 동아리 수정
def club_update(req, name):
    # 동아리 수정일 경우
    if req.method == 'POST':
        club_name = req.POST.get('club_name')
        club_admin = req.user  # 현재 세션 user
        club_info = req.POST.get('club_info')
        club_contents = req.POST.get('club_contents')
        club_loc = req.POST.get('club_loc')
        club_images = images = req.FILES.get('club_images')

        # 동아리 이미지를 변경하지 않음 / 기존 경로 사용
        if club_images is None:
            club_old = Club.objects.get(club_name=name)
            club = Club(club_name=club_name,
                        club_admin=club_admin,
                        club_info=club_info,
                        club_contents=club_contents,
                        club_loc=club_loc,
                        club_images=club_old.club_images,
                        )
            club.save()
            return redirect('club:club')

        # 동아리 이미지를 변경함 / 새로운 경로 설정
        else:
            club = Club(club_name=club_name,
                        club_admin=club_admin,
                        club_info=club_info,
                        club_contents=club_contents,
                        club_loc=club_loc,
                        club_images=club_images,
                        )
            club.save()
            return redirect('club:club')

    club = Club.objects.get(club_name=name)
    # GET / 동아리 수정 페이지 화면
    return render(req, 'club_update.html', {'club': club})


# 동아리 후기 작성
def club_post(req, name):
    if req.method == 'POST':
        club = Club.objects.get(club_name=name)  # path/club_name
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
        
        # 동아리 후기들의 평균을 해당 동아리 인스턴스의 점수로 저장
        club_score_avg = PostScript.objects.filter(club_name__club_name=name).aggregate(Avg('post_score'))
        # print(club_score_avg['post_score__avg'])
        club.club_score = club_score_avg['post_score__avg']
        club.save()
        return redirect('club:club_info', name)
    #
    return render(req, '')

