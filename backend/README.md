## Backend - django

- 디렉토리 구성도

  - backend: django project 설정

  - ../accounts : 계정 관리 dajngo app
  
  - ../contents : 컨텐츠 관리 django app
  
  - ../contents/tts : 텍스트 음성 합성 처리 ai 모듈

    
  
- 사용법

  - 프로젝트 루트로 이동 (requirements.txt가 존재하는 곳)

  - 파이썬 패키지 설치
  
    ```bash
    pip install -r requirements.txt
    # 개발환경
    pip install -r requirements_local.txt
    ```
  
  - DB 모델링
  
    ```bash
    python manage.py makemigration
    python manage.py migrate
    ```
  
  - 실행
  
    ```bash
    python manage.py runserver
    ```
  
    