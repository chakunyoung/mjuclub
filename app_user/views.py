from django.shortcuts import render, get_object_or_404


# 127.0.0.1:8000/user
def user(request):
    return render(request, 'user.html')


# 127.0.0.1:8000/user/userInfo
def userInfo(request):
    return render(request, 'userInfo.html')


def user_login(req):
    return render(req, 'userlogin.html')
                            # templates/userInfo.html 알아서 찾아서 감