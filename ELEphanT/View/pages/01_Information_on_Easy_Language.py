import streamlit as st

st.sidebar.markdown(" ")
st.markdown("# Easy Language in Germany")
st.markdown("#### Contents")
exp1 = st.expander("1. Definitions", expanded=True)
exp2 = st.expander("2. Target Groups")
exp3 = st.expander("3. Rulebooks")
exp4 = st.expander("4. Automatic Approaches to Easy Language")
with exp1:
    st.markdown("#### 1. Definitions")
with exp2:
    st.markdown("#### 2. Target Groups")
with exp3:
    st.markdown("#### 3. Rulebooks")
with exp4:
    st.markdown("#### 4. Automatic Approaches to Easy Language")
