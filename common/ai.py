import streamlit as st
from groq import Groq
from dotenv import load_dotenv

from .constants import ROLE

# Client는 인터넷 통신할 때 사용하는 용어
@st.cache_resource  # Sington 디자인 패턴 적용
def get_client():
    load_dotenv()   # 서비스에 .env 파일에 등록된 API 코드 적용
    return Groq()

def get_ai_msg(user_input:str, model_name:str="openai/gpt-oss-120b") -> str:
    # 이력 데이터 추가
    messages = [                # groq에선 key를 msg가 아닌 content로 전달해야함
        {                       # 실수래
            "role":history["role"].name,     # 얘는 ROLE 객체를 모르니 string으로 전달
            "content":history["msg"]        # 이건 string이 맞음
        } for history in st.session_state.history
    ]

    # 사용자 메세지 추가
    messages.append({
        "role":ROLE.user.name,
        "content":user_input
    })

    # groq clinet를 가져옴
    client = get_client()
    response = client.chat.completions.create(      # 응답 받기 (AI 메시지)
        messages = messages,
        model = model_name
    )

    return response.choices[0].message.content