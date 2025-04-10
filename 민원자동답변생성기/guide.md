# 생성 인공지능을 활용한 새올민원 자동답변 시스템 개발 가이드

이 가이드는 생성 인공지능을 활용한 새올민원 자동답변 시스템을 개발하려는 학생들을 위한 개발 가이드입니다. 시스템의 배경, 목적, 기술 요구사항 및 개발 단계를 상세히 설명합니다.

## 1. 프로젝트 개요

### 1.1 프로젝트 목표
지자체 공무원들이 민원 답변을 작성할 때 생성 인공지능을 활용하여 신속하고 품질 높은 답변을 생성할 수 있는 시스템을 개발합니다.

### 1.2 개발 배경 및 필요성
- 온라인 민원 접수의 폭발적 증가로 처리 업무 과중
- 민원 내용의 개인정보 보호 문제로 상용 AI 서비스 활용 불가
- 표준 서식에 맞는 답변 작성의 어려움
- 업무 과중으로 인한 답변 품질 저하 및 처리 기한 초과
- 신속하고 수준 높은 민원 답변을 위한 보조 시스템 필요

### 1.3 주요 기능
- 로컬 LLM을 활용한 민원 내용 이해 및 답변 생성
- 민원 카테고리별 맞춤형 답변 생성
- 답변 양식 자동 적용 및 커스터마이징
- 답변 히스토리 관리 및 통계 분석
- 부서 및 담당자 정보 자동 포함

## 2. 시스템 요구사항

### 2.1 서버 요구사항
- **운영체제**: Ubuntu Linux (22.04 LTS 권장)
- **하드웨어**: 
  - GPU: NVIDIA RTX 4090 이상 (로컬 LLM 구동용)
  - RAM: 32GB 이상
  - 저장공간: 500GB 이상 SSD
- **네트워크**: 폐쇄망 환경 구성 (개인정보 보호)
- **동시접속**: 최대 50명 지원

### 2.2 소프트웨어 요구사항
- **프로그래밍 언어**: Python 3.9 이상
- **웹 프레임워크**: Streamlit
- **AI 프레임워크**: 
  - Ollama (로컬 LLM 서비스)
  - LangChain (프롬프트 관리 및 LLM 연동)
- **데이터베이스**: SQLite 또는 PostgreSQL
- **버전 관리**: Git

## 3. 개발 단계 및 방법론

### 3.1 데이터 수집 및 전처리
- 공개민원데이터 크롤링 (사하구 새올전자민원창구 등)
  - URL: https://eminwon.saha.go.kr/emwp/gov/mogaha/ntis/web/emwp/cmmpotal/action/EmwpMainMgtAction.do
  - 민원조회 > 공개 상담민원 조회 섹션 활용
- 개인정보 제거 및 데이터 익명화
- 민원 카테고리 분류 및 라벨링
- 데이터 정제 및 포맷 표준화

### 3.2 LLM 선택 및 파인튜닝
- 적합한 오픈소스 LLM 선택 (Gemma, Llama3, Mistral 등)
- 민원 답변 데이터로 파인튜닝 진행
- 평가 및 성능 최적화
- Ollama 서비스 통합

### 3.3 UI 개발 (Streamlit)
- 직관적인 웹 인터페이스 설계
- 민원 입력 및 답변 생성 화면 구현
- 설정 및 커스터마이징 기능
- 히스토리 및 통계 대시보드

### 3.4 시스템 통합 및 최적화
- Ollama와 Streamlit 연동
- 응답 시간 최적화
- 메모리 사용량 관리
- 동시 접속 처리

## 4. 개발 로드맵

### 4.1 기본 버전 (MVP)
1. **Ollama 로컬 버전**
   - Ollama를 활용한 로컬 LLM 연동
   - 인터넷 없이 로컬에서 실행 가능
   - 기본 모델 (Gemma, Llama 등) 지원

### 4.2 고급 버전
1. **파인튜닝 모델 통합**
   - 민원 데이터로 파인튜닝된 모델 적용
   - 응답 품질 개선

2. **고급 기능 추가**
   - 민원 자동 분류
   - 답변 추천 시스템


## 5. 개발 시 주의사항

### 5.1 보안 및 개인정보
- 민원 데이터는 민감한 개인정보를 포함할 수 있으므로 반드시 익명화 처리
- 폐쇄망 환경에서만 운영
- API 키 등 중요 정보는 환경변수나 보안 저장소 활용

### 5.2 성능 최적화
- 대용량 LLM은 리소스 소모가 큼
- 응답 시간과 메모리 사용량 최적화 필요
- 모델 양자화(Quantization) 고려

### 5.3 사용자 경험
- 공무원이 쉽게 사용할 수 있는 직관적인 UI 설계
- 응답 대기 시간 최소화
- 오류 처리 및 피드백 메커니즘 구현

## 6. 참고 자료

- 시스템 설계 참고 영상: https://www.youtube.com/watch?v=VkcaigvTrug
- Streamlit 공식 문서: https://docs.streamlit.io/
- Ollama 프로젝트: https://ollama.com/
- LangChain 문서: https://langchain.com/docs
- 공개민원데이터: https://eminwon.saha.go.kr


---

이 개발 가이드를 참고하여 생성 인공지능을 활용한 새올민원 자동답변 시스템을 성공적으로 개발하시길 바랍니다. 