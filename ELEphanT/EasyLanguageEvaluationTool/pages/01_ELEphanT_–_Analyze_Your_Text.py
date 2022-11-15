import streamlit as st
import sys
sys.path.append("./PreProcessing/")
from TextPreprocessor import TextPreprocessor

st.sidebar.image("./ELEphanT_logo.png", width=300)
st.markdown("## ELEphanT: Analyze your Text")
exp3 = st.expander("3. Sentence Level Analysis")
exp4 = st.expander("4. Text Level Analysis")
st.markdown("##### Insert title")
title = st.text_input(label="title", label_visibility="collapsed")
if title:
    st.markdown("##### Insert text")
    st.info("Note: In submitting your text (pressing ctrl + enter) you agree that your text is preprocessed by ELEphanT. "
            "Preprocessing includes i.e. the substitution of french quotation marks (»«), which are commonly used in German literature, by German quotations („“).")
    st.markdown("**Press ctrl + enter to submit your text**")
    text = st.text_area(label="Insert your text", label_visibility="collapsed", height=350)
    if text and title:
        text_preprocessor = TextPreprocessor()
        preprocessed_text = text_preprocessor.preprocess_texts(text)
        st.markdown(f"Preprocessed Text: {preprocessed_text}")
        st.success("Preprocessing successful!")

        # Hier: LS-Evaluierung starten mit dem Input-Text
        # Die einzelnen Schritte ausgeben lassen als Info
        success = st.success("Evaluation successful!")
        if success:
            st.markdown("##### First glimpse on results")
            # TODO: display df.head()
            # TODO: download button, um excel-tabelle herunterzuladen.
