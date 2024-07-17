#처음에 부모로 선택하고 로그인하면 나오는 화면(가족내에서 진행 되는 모든 협상을 볼 수 있는 버튼, 진행중인 협상을 볼 수 있는 버튼)
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
if "username" not in st.session_state:
    st.session_state.username = 'null'
if "code" not in st.session_state:
    st.session_state.code = 'null'
if "type" not in st.session_state:
    st.session_state.type = 'null'
if st.session_state.type=='부모':
    st.title('Parent Dashboard')
    with st.container(border=True):
        st.page_link('pages/parents_negotiate.py',label='요청 확인하기')
        st.page_link('pages/log.py',label="기록보기")
    with st.container(border=True):
        st.header('미션 주기')
        st.text_input('미션명')
        name = st.text_input('이름')
        st.text_input('상품')
        if st.button('미션 보내기'):
            ref = db.reference('main').child(st.session_state.code)
            
elif st.session_state.type=='자녀':
    st.write('자녀')
else:
    st.error('로그인 후 이용 가능해요.')