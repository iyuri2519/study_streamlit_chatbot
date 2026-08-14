import streamlit as st
from .constants import ROLE

def show_msg(role:ROLE, msg:str, is_history=False) -> None:

    assert isinstance(role, ROLE), "정상적인 코드가 아닙니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    with st.chat_message(role.name):
        st.markdown(msg)

    if not is_history:
        st.session_state.history.append({           # 히스토리에 딕셔너리 저장
            "role":role,
            "msg":msg
        })
