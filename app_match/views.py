from django.shortcuts import render, get_object_or_404


def match(request):
    return render(request, 'match.html')