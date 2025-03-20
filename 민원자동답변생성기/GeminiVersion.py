import streamlit as st
import pandas as pd
from datetime import datetime
import requests
import json
import os

# Streamlit 앱 설정
st.set_page_config(page_title="민원 응답 생성기", page_icon="📝", layout="wide")

st.title("민원 응답 생성기")

# API 키 설정
if "GEMINI_API_KEY" not in st.session_state:
    st.session_state.GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# API 키 입력 필드
api_key = st.sidebar.text_input(
    "Google Gemini API 키 입력:", value=st.session_state.GEMINI_API_KEY, type="password"
)
if api_key:
    st.session_state.GEMINI_API_KEY = api_key
    os.environ["GEMINI_API_KEY"] = api_key

# 세션 상태 초기화
if "department" not in st.session_state:
    st.session_state.department = ""
if "tel" not in st.session_state:
    st.session_state.tel = ""
if "gemini_model" not in st.session_state:
    st.session_state.gemini_model = "gemini-1.5-pro"
if "history" not in st.session_state:
    st.session_state.history = []

st.sidebar.subheader("설정")

gemini_model = st.sidebar.selectbox(
    "Gemini 모델 선택 : ", ["gemini-2.0-flash"], index=0
)
# 사이드바에 민원 카테고리 선택 옵션 추가
category = st.sidebar.selectbox(
    "민원 카테고리", ["일반", "환경", "교통", "복지", "교육", "기타"]
)
# 도움말
department = st.sidebar.text_input("부서명을 입력하세요:", placeholder="부서명")
tel = st.sidebar.text_input(
    "담당자 행정 전화번호를 입력하세요:", placeholder="051-220-0000"
)
if st.sidebar.button("설정 저장"):
    st.session_state.department = department
    st.session_state.tel = tel
    st.session_state.gemini_model = gemini_model
    st.sidebar.success("설정이 저장되었습니다.")
    st.sidebar.success(f"선택된 모델: {st.session_state.gemini_model}")

st.sidebar.markdown("""---""")

if st.sidebar.button("히스토리 초기화"):
    st.session_state.history = []
    st.sidebar.success("히스토리가 초기화되었습니다.")

st.sidebar.markdown("""---""")

st.sidebar.subheader("도움말")
st.sidebar.info(
    "이 앱은 구청 공무원들이 민원에 대해 신속하고 적절한 답변을 생성하는 데 도움을 줍니다. "
    "민원 내용, 답변 양식, 답변 요지, 그리고 담당자의 역할을 입력하면 AI가 적절한 답변을 생성합니다."
)

# 입력 필드 생성
col1, col2 = st.columns(2)

default_role = """ 당신은 유능하고 친절한 공무원입니다. 
주어진 민원내용에 대해 [답변요지]를 바탕으로 적절한 답변을 마련하여 [답변양식]에 맞게 답변합니다."""

default_answer = f"""1. 귀하의 가정에 행복이 가득하시길 바랍니다.

2. 귀하의 민원내용은 [민원요지]에 관한 것으로 이해(또는 판단) 됩니다.

3. 귀하의 질의사항에 대해 검토한 의견은 다음과 같습니다.

 가. [답변내용]

4. 귀하의 질문에 만족스러운 답변이 되었기를 바라며, 답변 내용에 대한 추가 설명이 필요한 
   경우에는 사하구 {st.session_state.department}(☎{st.session_state.tel})에게 연락주시면 친절히 안내해 드리도록 
   하겠습니다.
   아울러 귀하의 민원처리에 대한 만족도 참여를 부탁드립니다. 
   감사합니다.
"""
placeholder_minwon = """새올민원 제목
새올민원 내용"""
placeholder_answer = """민원요지 : 00동 000로 00길 쓰레기 무단투기
답변요지: 현장확인 후 조속히 처리하겠음."""

with col1:
    role = st.text_area(
        "역할을 입력하세요:",
        value=default_role,
        height=200,
    )
    minwon = st.text_area(
        "민원 내용을 입력하세요:", placeholder=placeholder_minwon, height=200
    )
with col2:
    answer = st.text_area(
        "답변 요지를 입력하세요:", placeholder=placeholder_answer, height=200
    )
    answer_format = st.text_area(
        "답변 양식을 입력하세요:", value=default_answer, height=200
    )

# 민원 긴급도 선택
urgency = st.select_slider(
    "민원 긴급도", options=["매우 낮음", "낮음", "보통", "높음", "매우 높음"]
)


# Gemini API 호출 함수
def call_gemini_api(prompt, model, temperature=0.7):
    """Google Gemini API 호출 함수"""
    if not st.session_state.GEMINI_API_KEY:
        return None, "API 키가 필요합니다."

    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={st.session_state.GEMINI_API_KEY}"

    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "topP": 0.95,
            "topK": 40,
            "maxOutputTokens": 2048,
        },
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            result = response.json()
            if "candidates" in result and len(result["candidates"]) > 0:
                if "content" in result["candidates"][0]:
                    content = result["candidates"][0]["content"]
                    if "parts" in content and len(content["parts"]) > 0:
                        return content["parts"][0]["text"], None
            return None, "응답 형식이 예상과 다릅니다."
        else:
            return None, f"API 오류: {response.status_code} - {response.text}"

    except Exception as e:
        return None, f"오류 발생: {str(e)}"


# 답변 생성 함수
def generate_response():
    if not st.session_state.GEMINI_API_KEY:
        st.error("Google Gemini API 키를 입력해주세요!")
        return

    if minwon and answer_format and answer and role:
        # 프롬프트 생성
        prompt = f"""당신은 {role}입니다. 아래의 민원 내용에 대해 주어진 답변 요지를 정확히 준수하여 답변 양식에 맞게 답변을 생성해 주세요.
        민원 카테고리: {category}
        민원 긴급도: {urgency}
        민원 내용:
        {minwon}
        답변 양식:
        {answer_format}
        답변 요지:
        {answer}
        역할: {role}
        
        다음 사항을 고려하여 답변을 작성해주세요:
        1. 민원인의 감정을 고려하여 공감적인 표현을 사용하세요.
        
        답변:"""

        with st.spinner("답변을 생성 중입니다..."):
            try:
                response, error = call_gemini_api(prompt, st.session_state.gemini_model)

                if error:
                    st.error(f"오류: {error}")
                    return

                st.success("답변이 생성되었습니다!")
                st.write(response)

                # 히스토리에 추가
                st.session_state.history.append(
                    {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "category": category,
                        "urgency": urgency,
                        "minwon": minwon,
                        "response": response,
                    }
                )
            except Exception as e:
                st.error(f"답변 생성 중 오류가 발생했습니다: {str(e)}")
    else:
        st.warning("모든 필드를 입력해주세요.")


# 버튼 생성 및 이벤트 처리
if st.button("답변 생성"):
    generate_response()

# 히스토리 표시
st.subheader("답변 히스토리")
history_df = pd.DataFrame(st.session_state.history)
if not history_df.empty:
    st.dataframe(history_df)
else:
    st.info("아직 생성된 답변이 없습니다.")

# 답변 분석
if not history_df.empty:
    st.subheader("답변 분석")
    total_responses = len(history_df)
    category_counts = history_df["category"].value_counts()
    urgency_counts = history_df["urgency"].value_counts()

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"총 답변 수: {total_responses}")
        st.write("카테고리별 답변 수:")
        st.write(category_counts)
    with col2:
        st.write("긴급도별 답변 수:")
        st.write(urgency_counts)
