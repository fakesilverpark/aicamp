import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

st.title("가족과 함께하는 :green[용돈]협상하기!")

st.page_link("pages/all_c_or_p.py", label="시작하기")

if not firebase_admin._apps:#처음 한 번 데이터베이스 불러오기
    key_dict = json.loads(st.secrets["textkey"])
    cred = credentials.Certificate(key_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://coin-5f97c-default-rtdb.firebaseio.com/'#데이터베이스 주소 입력
    })

ref = db.reference('main')
if ref.child('').get():
    #이미 있음
    on = 1
else:
    ref.set({
        '가족코드':{
            '사용자 이름':{
                'type':'',
                'request':{
                }
            },
            '내역':{
            }
        }
    })


    