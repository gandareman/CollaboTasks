# 민원 응답 생성기

민원 응답 생성기는 구청 공무원들이 민원에 대해 신속하고 적절한 답변을 생성하는 데 도움을 주는 웹 애플리케이션입니다.

## 주요 기능

- **자동 답변 생성**: AI 모델을 활용하여 민원 내용에 맞는 공식 답변을 자동으로 생성
- **맞춤형 설정**: 부서명, 담당자 전화번호 등의 정보를 설정하여 답변에 자동 포함
- **민원 분류**: 카테고리 및 긴급도에 따른 민원 분류 기능
- **히스토리 관리**: 생성된 모든 답변의 히스토리 저장 및 관리
- **답변 분석**: 카테고리별, 긴급도별 답변 통계 제공

## 버전 안내

### 1. Google Gemini 버전 (GeminiVersion.py)
- Google Gemini API를 활용한 버전
- 인터넷 연결 필요
- Google Gemini API 키 필요

### 2. Ollama 로컬 버전 (ollamaVersion.py)
- Ollama를 활용한 로컬 실행 버전
- 인터넷 연결 없이 실행 가능
- Gemma3, Llama3 등 다양한 로컬 모델 지원
- 로컬 컴퓨터의 자원 사용

## 설치 방법

```bash
# 저장소 복제
git clone url.git

# 필요한 패키지 설치
pip install -r requirements.txt

# Ollama 버전 사용 시 추가 설치 (Windows/macOS/Linux)
# 1. Ollama 설치: https://ollama.com/download
# 2. 필요한 모델 다운로드
ollama pull gemma3:latest
ollama pull llama3:latest
```

## 사용 방법

### Google Gemini 버전 실행

1. Streamlit 앱 실행:
```bash
streamlit run GeminiVersion.py
```

2. 웹 브라우저에서 앱에 접속 (기본: http://localhost:8501)

3. Google Gemini API 키 입력 (사이드바)

4. 필요한 설정 (부서명, 전화번호 등) 입력

5. 민원 내용, 답변 요지, 카테고리 등 입력 후 '답변 생성' 버튼 클릭

### Ollama 로컬 버전 실행

1. Ollama 서비스 실행 확인 (Ollama 앱이 실행 중이어야 함)

2. Streamlit 앱 실행:
```bash
streamlit run ollamaVersion.py
```

3. 웹 브라우저에서 앱에 접속 (기본: http://localhost:8501)

4. 사용할 LLM 모델 선택 (gemma3:latest 또는 llama3:latest)

5. 필요한 설정 (부서명, 전화번호 등) 입력

6. 민원 내용, 답변 요지, 카테고리 등 입력 후 '답변 생성' 버튼 클릭

## 필요 사항

### Google Gemini 버전
- Python 3.7 이상
- Google Gemini API 키
- 인터넷 연결

### Ollama 버전
- Python 3.7 이상
- Ollama 설치
- 충분한 시스템 자원 (최소 8GB RAM, 권장 16GB 이상)

## 기술 스택

- **Frontend/Backend**: Streamlit
- **AI 모델**: 
  - Google Gemini API (클라우드 버전)
  - Ollama와 LangChain (로컬 버전)
- **데이터 처리**: Pandas

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 