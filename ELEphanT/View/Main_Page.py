import streamlit as st

st.markdown("# Easy Language in German Literature")
st.sidebar.markdown(" ")

container = st.container()
with container:
    st.write("This page functions as a web presentation for the tool I developed during a research project. "
                 "The tool offers the possibility to examine whether a given text complies to the rules of Easy Language. ")
    st.markdown("You will be able to: \n - Learn about Easy Language in Germany \n - Inspect my results regarding children's books \n"
                "- Use the tool to analyze your own text")

