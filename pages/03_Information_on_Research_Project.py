import streamlit as st
from pathlib import Path
from PIL import Image

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.set_page_config(layout="wide")
elephant_logo = Image.open("./ELEphanT_logo.png")
st.sidebar.image(elephant_logo, width=300)
st.markdown("## Evaluating Easy Language in Children's Books")
exp0 = st.expander("Overview", expanded=True)
exp1 = st.expander("I. Introduction")
exp2 = st.expander("II. Preprocessing")
exp3 = st.expander("III. Tool Implementation")
exp4 = st.expander("IV. Tool Evaluation")

with exp0:
    overview_md = read_markdown_file("./Markdown-Files/03_Overview.md")
    st.markdown(overview_md, unsafe_allow_html=True)
with exp1:
    introduction_md = read_markdown_file(
        "./Markdown-Files/03_Introduction.md")
    st.markdown(introduction_md, unsafe_allow_html=True)
with exp2:
    preprocessing_md = read_markdown_file(
        "./Markdown-Files/03_PreProcessing.md")
    st.markdown(preprocessing_md, unsafe_allow_html=True)
with exp3:
    implementation_md = read_markdown_file(
        "./Markdown-Files/03_Tool Implementation.md")
    st.markdown(implementation_md, unsafe_allow_html=True)
with exp4:
    evaluation_md = read_markdown_file(
        "./Markdown-Files/03_Tool Evaluation.md")
    st.markdown(evaluation_md, unsafe_allow_html=True)