import streamlit as st
from .show import show_msg

def init_history() -> None:
    # 만약 저장소에 history가 존재하지 않으면 history 선언
    if "history" not in st.session_state:
        st.session_state.history = []

    # history에 있는 모든 role-msg 데이터 출력
    for h in st.session_state.history:
        show_msg(**h, is_history=True)