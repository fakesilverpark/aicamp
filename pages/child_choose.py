#선물로 협상할지 용돈으로 협상할지 선택
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from openai import OpenAI
from dotenv import load_dotenv
import os
#지금 24년 7월 18일 목요일 오전 2시 32분인데 죽을거같다. 잠은 안오는데 죽을거 같다 살려줘라 
# load .env
load_dotenv()

API_KEY = os.environ.get('API_KEY')
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def callAI(reason,want):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "너는 부모님에게 선물을 요청하는 아이들이 요청하는 글을 좀 더 길게 쓸 수 있게 해 주는 AI야."},
        {"role": "user", "content": f"${reason}. 이 때문에 ${want}를 가지고싶은 10대 학생이 그것을 사달라고 부모님을 설득하기 위한 글을 써 줘. 제목은 쓰지마. 50자 이내로 써줘 예의 바르게 해"},
        ]
    )

    return response.choices[0].message.content

if "username" not in st.session_state:
    st.session_state.username = 'null'
if "code" not in st.session_state:
    st.session_state.code = 'null'
if "type" not in st.session_state:
    st.session_state.type = 'null'

if st.session_state.type == '자녀':
   tab1, tab2= st.tabs(["선물", "용돈"])

   with tab1:
      st.title('부모님과 선물 협상하기')
      want = st.text_input("본인이 원하는 선물의 이름을 적어주세요!", "")
      want_price = st.text_input("본인이 원하는 선물의 가격을 적어주세요!", "")
      reason=st.text_area("선물 요청 글 작성이 완료되면 command+enter를 눌러주세요",height=5)
      if st.button('선물 글 다듬기/전송'):
         txt = callAI(reason,want)
         st.write(txt)
         ref = db.reference('main').child(st.session_state.code)
         if ref.get():
            ref = ref.child(st.session_state.username)
            if ref.child('request').get():
               ref.child('request').child('present').update({
                  want:{
                     'price':want_price,
                     'text':txt,
                     'type':'present'
                  }
               })
            else:
               ref.update({
                  'request':{
                     'present':{
                        want:{
                           'price':want_price,
                           'text':txt,
                           'type':'present'
                     }
                     }
                  }
               })
            st.success('전송에 성공했어요.')

   with tab2:
      st.title('부모님과 용돈 협상하기')
      want_pri = st.text_input("본인이 원하는 용돈의 가격을 작성해주세요!", "")
      reason=st.text_area("용돈 작성이 완료되면 command+enter를 눌러주세요",height=5)
      want = '돈'
      if st.button('용돈 글 다듬기/전송'):
         txt = callAI(reason,want)
         st.write(txt)
         ref = db.reference('main').child(st.session_state.code)
         if ref.get():
            print(txt)
            ref = ref.child(st.session_state.username)
            if ref.child('request').get():
               ref.child('request').child('money').update({
                     'price':want_pri,
                     'text':txt
               })
            else:
               ref.update({
                  'request':{
                     'money':{
                           'price':want_pri,
                           'text':txt
                     }
                     
                  }
               })
            st.success('전송에 성공했어요.')
elif st.session_state.type == '부모':
   st.error('권한이 부족합니다.')
