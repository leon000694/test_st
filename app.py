print() # streamlit run D:\Python\網站開發\streamlit\env-testapp\test_app.py
# 虛擬環境: *(建立) python -m venv env-test_project *(激活) D:\Python\網站開發\st_test_project\env-test_project\Scripts\Activate.ps1 *(去活) path> deactivate
# pip install streamlit
import streamlit as st

st.set_page_config(
    page_title="Test app",
    page_icon =":shark:")
st.title('M13 資訊交流網頁 3')
st.write('Hello world')
st.markdown("Hello **world**!")
selected = st.checkbox("I agree")
choices = st.multiselect("Buy", ["milk","apple","potatoes"])
choice  = st.selectbox("Pick one", ["cats","dogs"])
text = st.text_area("Text to translate")
name = st.text_input("First name")
data = st.file_uploader("Upload a CSV")
st.success("Match found!")
st.info("Dataset is updated every day at midnight")
css = """
<style>
    p {color: red;}
</style>
"""
st.html(css)