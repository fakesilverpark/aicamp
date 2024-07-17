#가족코드 생성, 본인 이름 작성
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
if not firebase_admin._apps:#처음 한 번 데이터베이스 불러오기
    st.session_state.username = 'null'
    st.session_state.code = 'null'
    st.session_state.type = 'null'
    key_dict = json.loads(st.secrets["textkey"])
    cred = credentials.Certificate(key_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://coin-5f97c-default-rtdb.firebaseio.com/'#데이터베이스 주소 입력
    })

if st.session_state.type == 'null':
    tab1, tab2= st.tabs(["Login", "SignUp"])

    with tab1:
        st.header("Login")
        inname = st.text_input('이름')
        incode = st.text_input('가족 코드')
        if st.button('로그인'):
            ref = db.reference('main')
            if ref.child(incode).get():
                if ref.child(incode).child(inname).get():  
                    st.session_state.username = inname
                    st.session_state.type = ref.child(incode).child(inname).child('type').get()
                    st.session_state.code = incode
                    st.switch_page('pages/2_dashboard.py')
                else:
                    st.error('없는 이름입니다.')
            else:
                st.error('없는 코드입니다.')
    with tab2:
        st.header("Sign Up")
        name = st.text_input('가입할 이름')
        code = st.text_input('가입할 가족 코드')
        type = st.radio('유형',['부모','자녀'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True) 
        st.caption('처음이시라면 가입, 가족에 참가하시려면 참가 버튼을 눌러주세요.')
        with st.container():
            st.write("      ")
            st.write("      ")
            col1, col2, col3, col4, col5, col6, col7, col8= st.columns(8)
            list=[col3, col4, col5, col6, col7, col8]

            for i in list:
                with i:
                    st.write("      ")
            with col1:
                if st.button('가입'):
                    ref = db.reference('main')
                    if ref.child(code).get():
                        st.error('이미 있는 코드입니다.')
                    else:
                        if ref.child(code).child(name).get():
                            st.error('이미 있는 이름입니다.')
                        else:
                            ref.update({
                                code:{
                                    name:{
                                        'type':type,
                                        'request':{
                                        }
                                    },
                                    'log':{
                                    }
                                }
                            })
            with col2:
                if st.button('참가'):
                    
                    ref = db.reference('main')
                    if ref.child(code).get():
                        if ref.child(code).child(name).get():
                            st.error('이미 있는 이름입니다.')
                        else:
                            ref.child(code).update({
                                name:{
                                        'type':type,
                                        'request':{
                                        }
                                    }
                            })
                    else:
                        st.error('없는 코드입니다.')

    st.write("      ")
    st.write("      ")
    col1, col2, col3, col4, col5, col6, col7, col8= st.columns(8)
    list=[col1, col2, col3, col4, col5, col6, col7]

    with col8:
        st.page_link("main.py", label="뒤로가기", icon="👈🏻")

    for i in list:
        with i:
            st.write("      ")
else:
    if st.button('로그아웃'):
        st.session_state.username = 'null'
        st.session_state.code = 'null'
        st.session_state.type = 'null'
        st.switch_page('pages/1_user.py')