import streamlit as st

st.sidebar.markdown(" ")
st.markdown("# Easy Language in Children's Books. \n ### Correlations between Age and Text Complexity?")

st.markdown("#### Contents")
exp1 = st.expander("1. Project Planning")
exp2 = st.expander("2. Data Selection")
exp3 = st.expander("3. Literature Research")
exp4 = st.expander("4. Formalisation / Concept")
exp5 = st.expander("5. Implementation")
exp6 = st.expander("6. Visualization")
exp7 = st.expander("7. Readability Correlation")
exp8 = st.expander("8. Sentiment Correlation")
with exp1:
    st.markdown("#### 1. Project Planning")
with exp2:
    st.markdown("#### 2. Data Selection")
with exp3:
    st.markdown("#### 3. Literature Research")
with exp4:
    st.markdown("#### 4. Formalisation / Concept")
with exp5:
    st.markdown("#### 5. Implementation")
with exp6:
    st.markdown("#### 6. Visualization")
with exp7:
    st.markdown("#### 7. Readability Correlation")
with exp8:
    st.markdown("#### 8. Sentiment Correlation")
