#부모가 자녀에게 받은 협상을 거절 및 승인하고 그에 대한 이유를 작성 할 수 있음
import random
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import json


if "username" not in st.session_state:
    st.session_state.username = 'null'
if "code" not in st.session_state:
    st.session_state.code = 'null'
if "type" not in st.session_state:
    st.session_state.type = 'null'
if "agree" not in st.session_state:
    st.session_state.agree = None
if st.session_state.type == "부모":
    st.title('요청 내역')
    ref = db.reference('main').child(st.session_state.code)
    users = ref.get()
    userdump = json.dumps(users)
    userdata = json.loads(userdump)
    for val,re in userdata.items():
        if val!='log':
            if re['type']=='자녀':
                name = ref.child(val).child('request').child('present').get()
                if name!=None:
                    for val2,re2 in name.items():
                        with st.container(border=True):
                            st.header(val)
                            st.subheader(val2 +' - '+re2['price']+'원')
                            st.write(re2['text'])
                            if re2['type']=='misson':
                                if st.button('수락'):
                                    ref.child(val).child('gift').update({
                                        val2:val2
                                    })
                                    if ref.child('log').get():
                                        ref.child('log').update({
                                            val2:{
                                                'text':re2['text'],
                                                'name':val,
                                                'type':'acc',
                                                'time':time.time()
                                            }
                                        })
                                    else:
                                        ref.update({
                                            'log':{
                                                val2:{
                                                    'text':re2['text'],
                                                    'name':val,
                                                    'type':'acc',
                                                    'time':time.time()
                                                }
                                            }
                                        })
                                    ref.child(val).child('request').child('present').child(val2).delete()
                                    st.switch_page('pages/parents_negotiate.py')
                            else:
                                if st.button(val+"에게 선물 보내기"):
                                    if ref.child('log').get():
                                        ref.child('log').update({
                                            val2:{
                                                'text':re2['text'],
                                                'name':val,
                                                'type':'acc',
                                                'time':time.time()
                                            }
                                        })
                                    else:
                                        ref.update({
                                            'log':{
                                                val2:{
                                                    'text':re2['text'],
                                                    'name':val,
                                                    'type':'acc',
                                                    'time':time.time()
                                                }
                                            }
                                        })
                                    ref.child(val).child('request').child('present').child(val2).delete()
                                    st.switch_page('pages/parents_negotiate.py')
                                if st.button(val+"의 선물 협상 거절하기"):
                                    if ref.child('log').get():
                                        ref.child('log').update({
                                            val2:{
                                                'text':re2['text'],
                                                'name':val,
                                                'price':re2['price'],
                                                'type':'blo',
                                                'time':time.time()
                                            }
                                        })
                                    else:
                                        ref.update({
                                            'log':{
                                                val2:{
                                                    'text':re2['text'],
                                                    'name':val,
                                                    'price':re2['price'],
                                                    'type':'blo',
                                                    'time':time.time()
                                                }
                                            }
                                        })
                                    if ref.child(val).child('re').get():
                                        ref.child(val).child('re').update({
                                            val2:{
                                                    'price':re2['price'],
                                                    'text':re2['text']
                                                }
                                        })
                                    else:
                                        ref.child(val).update({
                                            're':{
                                                val2:{
                                                    'price':re2['price'],
                                                    'text':re2['text']
                                                }
                                            }
                                        })
                                    ref.child(val).child('request').child('present').child(val2).delete()
                                    st.switch_page('pages/parents_negotiate.py')
                name = ref.child(val).child('request').child('money').get()
                if name!=None:
                    with st.container(border=True):
                        st.header(val)
                        st.subheader(name['price'])
                        st.write(name['text'])
                        if st.button(val+"에게 용돈 보내기"):
                            if ref.child('log').get():
                                ref.child('log').update({
                                    val+'-'+name['price']+'-'+"용돈"+'-'+str(random.randint(0, 10000)):{
                                            'text':name['text'],
                                            'name':val,
                                            'price':name['price'],
                                            'type':'acc',
                                            'time':time.time()
                                        }
                                    })
                                st.success('요청을 성공적으로 처리했어요.')
                                ref.child(val).child('request').child('money').delete()
                                st.switch_page('pages/parents_negotiate.py')
                            else:
                                ref.update({
                                    'log':{
                                        val+'-'+name['price']+'-'+"용돈"+'-'+str(random.randint(0, 10000)):{
                                            'text':name['text'],
                                            'name':val,
                                            'price':name['price'],
                                            'type':'acc',
                                            'time':time.time()
                                        }
                                    }
                                })
                                st.success('요청을 성공적으로 처리했어요.')
                                ref.child(val).child('request').child('money').delete()
                                st.switch_page('pages/parents_negotiate.py')
                        if st.button(val+"의 용돈 협상 거절하기"):
                                if ref.child('log').get():
                                    ref.child('log').update({
                                        val+'-'+name['price']+'-'+"용돈"+'-'+random.randint(0, 10000):{
                                            'text':name['text'],
                                            'name':val,
                                            'price':name['price'],
                                            'type':'blo',
                                            'time':time.time()
                                        }
                                    })
                                    st.success('요청을 성공적으로 처리했어요.')
                                    ref.child(val).child('request').child('money').delete()
                                    st.switch_page('pages/parents_negotiate.py')
                                else:
                                    ref.update({
                                        'log':{
                                            val+'-'+name['price']+'-'+"용돈"+'-'+random.randint(0, 10000):{
                                            'text':name['text'],
                                            'name':val,
                                            'price':name['price'],
                                            'type':'blo',
                                            'time':time.time()
                                        }
                                        }
                                    })
                                    st.success('요청을 성공적으로 처리했어요.')
                                    ref.child(val).child('request').child('money').delete()
                                    st.switch_page('pages/parents_negotiate.py')
                        
elif st.session_state.type == "자녀":
    st.error('자녀는 이용할 수 없어요.')
else:
    st.error('로그인 후 이용 가능해요.')