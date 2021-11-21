from django.shortcuts import render, get_object_or_404


def match(req):
    return render(req, 'match.html')


def match_result(req):
    feature_list =[]
    if req.method == 'POST':
        feature0 = req.POST.get('feature0')  # 개방
        feature1 = req.POST.get('feature1')  # 친화
        feature2 = req.POST.get('feature2')  # 정서
        feature3 = req.POST.get('feature3')  # 성실
        feature4 = req.POST.get('feature4')  # 외향

        print(feature0)
        feature_list = [feature0, feature1, feature2, feature3, feature4]
        print(feature_list)

    return render(req, 'match_result.html', {"feature_list": feature_list})