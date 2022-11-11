import streamlit as st

#st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Logo/ELEphanT_logo_no writing.png", width=440)
with col2:
    st.markdown("# ELEphanT \n ### Easy Language Evaluation Tool")
    st.write("This page functions as a web presentation for the tool I developed during a universitary research project. "
                 "The tool offers the possibility to examine to what degree a given text complies to the rules of Easy Language. ")
    st.markdown("You will be able to: \n - Use the tool to analyze your own text \n - Learn about Easy Language in Germany "
                "\n - Read about the details of my research project on the basis of children's books")
st.sidebar.markdown(" ")
