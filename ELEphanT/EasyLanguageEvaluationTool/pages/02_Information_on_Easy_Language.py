import streamlit as st
from pathlib import Path
from PIL import Image

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.set_page_config(layout="wide")
elephant_logo = Image.open("./ELEphanT_logo.png")
st.sidebar.image(elephant_logo, width=300)
st.markdown("# What is Easy Language?")

easy_language_markdown = read_markdown_file("./Markdown-Files/Easy Language.md")
st.markdown(easy_language_markdown, unsafe_allow_html=True)