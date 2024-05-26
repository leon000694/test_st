print() 
#1 streamlit run D:\Python\網站開發\st_test_project\app.py
#2 streamlit run https://github.com/leon000694/test_st/blob/main/app.py
# 虛擬環境: *(建立) python -m venv env-test_project *(激活) D:\Python\網站開發\st_test_project\env-test_project\Scripts\Activate.ps1 *(去活) path> deactivate
# pip install streamlit
import streamlit as st
st.set_page_config(
    page_title="Test app",
    page_icon =":shark:")

st.title   ('(Test) M13 資訊交流網頁 6')
st.markdown("Hello **world** !")
selected= st.checkbox   ("勾選")
choices = st.multiselect("待買-多選", ["milk","apple","potatoes"])
choice  = st.selectbox  ("選擇-單選", ["cats","dogs"])
text = st.text_area("每日記事")

name = st.text_input("輸入 First name")
data = st.file_uploader("上傳 a CSV")
st.success("Match found!")
st.info("資料庫 is updated every day at midnight")
css = """
<style> p {color: blue;} </style>"""
st.html(css)