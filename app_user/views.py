from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout


# 유저 메인
# 127.0.0.1:8000/user
def user(request):
    return render(request, 'user.html')


# 유저 정보
# 127.0.0.1:8000/user/userInfo
def user_info(request):
    return render(request, 'user_info.html')


# 유저 로그인
def user_login(req):
    # 로그인 버튼 클릭 시
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)  # db와 검증해서 있다면 user 객체를 반환
        if user is not None:
            login(req, user)  # 로그인 / 세션id 생성 / 쿠키에 세션id 저장
            print("session id= " + user.get_session_auth_hash())
            return redirect('main:main')
        else:
            print("인증실패")
            return render(req, 'user_login.html')  # 로그인 인증 실패시 다시 로그인 화면으로

    # 로그인 화면
    return render(req, 'user_login.html')


# 유저 회원가입
def user_signup(req):
    # 회원가입 버튼 동작
    if req.method == 'POST':
        username = req.POST.get('username')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        selected = req.POST.getlist('selected[]')
        # 일반 사용자
        if not selected:
            selected = False
        # 동아리 운영자
        else:
            selected = True

        # 아이디 검증
        if User.objects.all().filter(username=username).exists():
            message = "아이디가 이미 존재함"
            return render(req, 'user_signup.html', {'message_id': message})

        # 비밀번호 검증
        if password1 == password2:
            user = User.objects.create_user(
                username=username,
                password=password1,
                is_club_admin=selected)
            user.save()
            message = "아이디가 생성됨"
        else:
            message = "비밀번호가 맞지 않음"
            return render(req, 'user_signup.html', {'message_pass': message})
        # 가입완료 / 메인화면으로 복귀
        return render(req, 'main.html', {'message': message})

    # 가입 화면
    return render(req, 'user_signup.html')


# 유저 로그아웃
def user_logout(req):
    logout(req)
    return redirect('main:main')