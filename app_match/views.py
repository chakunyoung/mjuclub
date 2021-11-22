from django.shortcuts import render, get_object_or_404
import numpy as np
import pandas as pd
import tensorflow as tf
from app_club.models import Club
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # tensorflow 오류 메세지 안나게


def match(req):
    return render(req, 'match.html')


def match_result(req):
    feature_list = []
    listf = []
    df = ''

    # Dependable - 0, Serious - 1, Responsible - 2, Extraverted - 3, Lively - 4, normal - 5
    per_club_match = {0: ['봉사', '종교', '교육', '공부', ],
                      1: ['사진', '영상', '종교', '문화', ],
                      2: ['봉사', '교육', '토론', '공부', ],
                      3: ['운동', '레저', '토론', '여행', '음악', ],
                      4: ['운동', '레저', '여행', '음악', ],
                      5: ['봉사', '사진', '영상', '기타', ],
                      'message': ['믿을만한', '진지한', '책임감있는', '외향적인', '활기친', '평범한']
                      }

    # from 입력값 Dataframe으로
    if req.method == 'POST':
        feature0 = req.POST.get('feature0')  # 개방성
        feature1 = req.POST.get('feature1')  # 친화성
        feature2 = req.POST.get('feature2')  # 정서적 안정성
        feature3 = req.POST.get('feature3')  # 성실성
        feature4 = req.POST.get('feature4')  # 외향성
        feature_list = [[feature0, feature1, feature2, feature3, feature4]]
        listf = np.float_(feature_list)
        df = pd.DataFrame(listf)  # 모델 입력 df
        
    # 모델 로드, 가중치 로드 // 재 학습시 이 부분만 변경
    model = tf.keras.models.load_model('app_match/modeldata/pers_model.h5')
    model.load_weights('app_match/modeldata/pers_weight.h5')

    # 모델 predictss
    model_pred = model.predict(df)
    model_pred_label = tf.keras.backend.eval(tf.argmax(model_pred, axis=1))
    predict_result = model_pred_label[0]  # 모델결과 label
    
    # 위에서 만든 dict 사용
    club_list = per_club_match[predict_result]  # 모델의 결과(key) 동아리목록(value)
    clubs = Club.objects.filter(club_info__in=club_list)  # 존재하는 동아리 유형만 filter
    result_label = per_club_match['message'][predict_result]   # int to 결과 성격 유형

    return render(req, 'match_result.html', {'clubs': clubs,
                                             'label': result_label,
                                             })