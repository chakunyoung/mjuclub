## 캡스톤디자인2 프로젝트

### 참여 인원: 2인

## 기술 스택
<img src="https://img.shields.io/badge/Python-4479A1?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Django-4479A1?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/TensorFlow-4479A1?style=for-the-badge&logo=TensorFlow&logoColor=white">
<img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

<br>

### 프로젝트 개요
동아리 가입을 원하는 사용자는 다양한 동아리들의 정보를 제공받으며, 매칭 기능을 이용하여 사용자 성격에 따른 동아리를 추천 받으며, <br>사용자 성격 유형과 어울러질 수 있는 적합한 요소를 가진 동아리를 추천받는 것을 목적으로 한다.

<br>

### 아키텍처
![아키텍처 다이어그램](images/architecture.jpg)

<br>

### 사용된 성격 유형 분류체계 OCEAN
![OCEAN 모델](images/ocean.jpg)

<br>

### 프로젝트 결과
![사용자 매칭 결과](images/user_maching.jpg)

<br>

### DNN 구성
![모델 구성도](images/model.jpg)
![모델 정확도](images/model_accu.jpg)

<br><br>

#### 실행시 필요한 작업

>pip install -r requirements.txt


#### 필요한 파일 (공개하지 않음)

>mysql.cnf<br>
>secrets.json


#### Model, Weight 경로

>app_match/modeldata

