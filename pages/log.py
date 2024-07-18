#가족내의 모든 협상내역을 볼 수 있다
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

if st.session_state.type != "null":
    st.title('활동 내역')
    ref = db.reference('main').child(st.session_state.code).child('log')
    users = ref.get()
    userdump = json.dumps(users)
    userdata = json.loads(userdump)
    if userdata:
        for val,re in userdata.items():
            with st.container(border=True):
                st.header(re['name'])
                st.subheader(val)
                if re['type']=='acc':
                    st.write('수락')
                else:
                    st.write('거부')
else:
    st.error('로그인 후 이용 가능해요.')