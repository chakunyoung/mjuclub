from django.shortcuts import render, get_object_or_404


def main(request):
    return render(request, 'main.html')


# 테스트
def test(request):
    return render(request, 'maintest.html')


