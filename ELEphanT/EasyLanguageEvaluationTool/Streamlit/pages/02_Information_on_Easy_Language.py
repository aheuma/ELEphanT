import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.sidebar.image("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Logo/ELEphanT_logo.png", width=300)
st.markdown("# What is Easy Language?")

easy_language_markdown = read_markdown_file(
    "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/ELEphant - Streamlit/ELEphanT/ELEphanT/EasyLanguageEvaluationTool/Streamlit/Markdown-Files/Easy Language.md")
st.markdown(easy_language_markdown, unsafe_allow_html=True)