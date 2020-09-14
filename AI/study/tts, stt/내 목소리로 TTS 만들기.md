## 내 목소리로 TTS 만들기

##### 음성 녹음

- 도커 설치

- 음성 녹음 (원하는 데이터 시간 * 2.5배 정도 소요)

  - https://github.com/sce-tts/mimic-recording-studio/archive/master.zip

  - 압축 풀고 ```start-windows.bat```파일 실행

  - 명령 프롬프트 중간에 `You can now view mimic-recording-studio in the browser.`라는 메시지가 출력되면, `http://localhost:3000/`에 접속하여 mimic-recording-studio를 사용할 수 있습니다.

- 음성 데이터셋 변환

  - 파일 탐색기로 Mimic Recording Studio의 `start-windows.bat` 파일이 있는 폴더를 엽니다.
  - 폴더 내의 빈 공간을 키보드 시프트 키를 누른 상태로 우클릭합니다.
  - 나타난 메뉴에서 `여기에 PowerShell 창 열기` 또는 `여기에서 명령 프롬프트 창 열기`를 선택합니다.
  - 열린 PowerShell 창 또는 명령 프롬프트 창은 잠시 그대로 두고, 파일 탐색기에서 `backend/audio_files` 폴더를 엽니다.
  - `audio_files` 폴더 내부에 존재하는 폴더 이름을 복사해둡니다.
    (예시: `110d3ec5-4a5a-0f63-a8a1-13345418c85b`)
  - 열린 PowerShell 창 또는 명령 프롬프트 창에 `docker-compose run --rm backend generate_ljs_audio_text.py <복사한 폴더 이름>`을 입력합니다.
    (예시: `docker-compose run --rm backend generate_ljs_audio_text.py 110d3ec5-4a5a-0f63-a8a1-13345418c85b`)
  - 실행이 완료될 때까지 기다립니다.
  - 위 과정을 완료하면, `backend` 폴더 내부에 `filelists` 폴더가 생성됩니다.



##### 머신러닝 수행 (구글 코랩 사용)

- 사전 준비

  - google drive에 ```Colab Notebooks```폴더 생성
  - 그 안에 ```data```폴더 생성
  - 위의 음성 데이터셋 알집 파일(제목은 ```filelists```)로 넣어두기

- glow-tts 학습

  - [SCE-TTS: Glow-TTS 학습 Colab](https://colab.research.google.com/drive/1IlZt42ETvNHthRFXfwNSSH-ftWthxzqr?usp=sharing)

  - 드라이브로 복사 & 런타임 유형 gpu 확인

    ** 학습 시 file path 오류 발생 시 왼쪽 사이드바 열어서 폴더 구조 확인 (google drive에 잘 저장했더라도 알집 파일 구조때문에 달라질 수 있음)

    ** 구글 드라이브 용량 초과될 수 있기 때문에 중간에 파일 삭제해야 할 수 있음

- multi-band melgan 학습

  - [SCE-TTS: Multi-band MelGAN 학습 Colab](https://colab.research.google.com/drive/1UinTd1Kp1ytwPQ4QWA610ZKOVfmPDdn5?usp=sharing)
  - 드라이브로 복사 & 런타임 유형 gpu 확인

##### 테스트

- [SCE-TTS: 음성합성 데모 Colab](https://colab.research.google.com/drive/13pqat2mWsMha7Vn_-Q5_Ih8MDkvz3q5a?usp=sharing)
- 드라이브로 복사



#### 원문: https://sce-tts.github.io/#/uses