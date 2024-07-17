#처음에 부모로 선택하고 로그인하면 나오는 화면(가족내에서 진행 되는 모든 협상을 볼 수 있는 버튼, 진행중인 협상을 볼 수 있는 버튼)
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

@st.experimental_dialog("상세 내용")
def misson_display():
    ref = db.reference('main').child(st.session_state.code).child(st.session_state.username).child('misson')
    st.header(ref.get())

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
        misson_name = st.text_input('미션명')
        name = st.text_input('이름')
        present = st.text_input('상품')
        text = st.text_area('내용',height=5)
        if st.button('미션 보내기'):
            ref = db.reference('main').child(st.session_state.code)
            if ref.child(name).child('misson').get():
                st.error('이미 미션을 할당했어요. 이전 미션이 끝난 후 다시 시도해주세요.')
            else:
                ref.child(name).child('misson').update({
                    misson_name:{
                        'present':present,
                        'text':text
                    }
                })
elif st.session_state.type=='자녀':
    st.title("Child Dashboard")
    with st.container():
        st.header('현재 진행 중인 미션')
        ref = db.reference('main').child(st.session_state.code).child(st.session_state.username).child('misson').get()
        if ref:
            st.write('1 개')
        else:
            st.write('0 개')
        if st.button('자세히 보기'):
            misson_display()
    st.divider()

    st.write("      ")
    st.subheader("지금까지 진행한 협상들을 보러가시겠습니까?")
    st.page_link("pages/log.py", label="➞ 협상내역 보러가기", icon="📂")
    st.write("      ")

    st.subheader("새로운 협상을 진행하시겠습니까?")
    st.page_link("pages/child_choose.py", label="➞ 부모님과 새로운 협상하러가기", icon="🗣️")

    st.write("      ")
    st.write("      ")
    col1, col2, col3, col4, col5, col6, col7, col8= st.columns(8)
    list=[col1, col2, col3, col4, col5, col6]

    with col8:
        st.page_link("main.py", label="홈", icon="🏠")

    with col7:
        st.page_link("pages/1_user.py", label="뒤로가기", icon="👈🏻")

    for i in list:
        with i:
            st.write("      ")
    
else:
    st.error('로그인 후 이용 가능해요.')