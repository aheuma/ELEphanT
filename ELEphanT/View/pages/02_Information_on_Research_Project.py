import streamlit as st

st.sidebar.markdown(" ")

st.markdown("# Project Background")
st.markdown("#### Contents")
exp1 = st.expander("1. Project Background", expanded=True)
exp2 = st.expander("2. Current Research Project", expanded=True)
with exp1:
    st.markdown("#### Project")
    st.markdown("##### CHYLSA: Children's and Youth Literature Sentiment Analysis")
    st.markdown("**Full title**: Advanced sentiment analysis for understanding affective-aesthetic responses to literary texts: A computational and experimental psychology approach to children’s literature")
    st.markdown("#### Project Description")
    st.markdown("Emotional involvement is of pivotal importance when children learn to read, tell, and share stories. This crucial dimension of cultural literacy has received surprisingly little attention within literary studies, psychology, and digital humanities. Taking a large-scale and data-driven approach, we develop and validate in CHYLSA AI-based sentiment analysis for computational literary studies. Our testcase are children´s books.")
    st.markdown("#### Project Duration")
    st.markdown("2019–2023")
    st.markdown("#### Project Associates")
    st.markdown("Mainz \n - Prof. Dr. Gerhard Lauer \n - Marina Lehmann M.A.")
    st.markdown("Berlin \n - Prof. Dr. Arthur Jacobs \n - Dr. Jana Lüdtke \n - Dr. Lisa Luther")

with exp2:
    st.markdown("- Research project is part of the master's program 'Digitale Methodik in den Geistes- und Kulturwissenschaften' (Digital Humanities) at JGU Mainz")
    st.markdown("- Duration: 13.09.2022–15.12.2022 (10 weeks overall with break)")
    st.markdown("- Use case: 28 books for younger children from childLex corpus \n \t - 14 books are for age 6–8 \n \t - 14 books are for age 10–12 ")
    st.markdown("- **Goals:** \n 1. On the basis of a chosen ruleset for Easy Language: measure the degree of Easy Language in a given text. \n "
                "2. Examine the differences between the two age groups and their text complexity / readabilty (measured as the degree of Easy Language. \n"
                "3. Research question: Do books for younger children comply more to the rules of Easy Language than books for older children?")