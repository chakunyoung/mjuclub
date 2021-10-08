from django.shortcuts import render, get_object_or_404


def club(request):
    return render(request, 'club.html')