import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

if not firebase_admin._apps:#처음 한 번 데이터베이스 불러오기
    key_dict = json.loads(st.secrets["textkey"])
    cred = credentials.Certificate(key_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'databaseURL'#데이터베이스 주소 입력
    })



    