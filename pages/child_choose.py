#선물로 협상할지 용돈으로 협상할지 선택
import streamlit as st

st.title('부모님과 협상하기')

tab1, tab2= st.tabs(["Money", "Gift"])

with tab1:
   st.title('부모님과 용돈 협상하기')
   st.header("Money")

with tab2:
   st.title('부모님과 선물 협상하기')
   st.header("Gift")
