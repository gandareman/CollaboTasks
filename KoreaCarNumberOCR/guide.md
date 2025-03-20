# 차량번호 OCR 프로그램

## 제안 주제
- **개인 PC 기반** 차량 번호판 인식 OCR 프로그램 개발

## 필요 기술
- 언어: Python
- 모듈: yolov5, streamlit, easyocr, pytorch, opencv, numpy

## 개발 배경 및 필요성
- 기존 chatGPT와 같은 SaaS 기반 프로그램은 개인정보보호 문제로 차량 사진 입력이 어려움.  
- 오픈소스 OCR 프로그램은 외국 차량 번호판 인식률은 높지만, 한국 차량 번호판 인식 성능은 떨어지거나 유료인 경우가 많음.
- **개인 PC에서**  쉽게 사용할 수 있고, **CPU 및 GPU 환경 모두**에서  작동하는  한국 차량 번호판 OCR 프로그램이 필요.

## 개발 요구사항
- 프로그램 형태: Python Streamlit 웹 UI(Localhost 동작 가능)
- 주요 기능:
    - 차량 사진에서 번호판 영역 자동 감지
    - 감지된 번호판 이미지에서 차량 번호 텍스트 추출
    - 대량의 파일(zip 파일 형식, 또는 복수의 이미지 파일) 업로드 시 자동으로 번호 텍스트 추출
- 참고 사항
    - 오픈소스 개발 사례: [Easy Korean License Plate Detector](https://github.com/gyupro/EasyKoreanLpDetector)
    - 차량 번호 데이터셋: [자동차 차종/연식/번호판 인식용 영상](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=172)

## 비고
- github을 통해 배포, 차량번호판 자동인식이 필요한 지자체에 배포