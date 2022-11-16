import lamda as lamda
import numpy as np
import streamlit as st
import sys
sys.path.append("./PreProcessing/")
sys.path.append("./Model/")
from TextPreprocessor import TextPreprocessor
from EasyLanguageEvaluator import EasyLanguageEvaluator
import pandas as pd

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
        #TODO: Auswählen lassen, ob man preprocessed text sehen möchte
        easy_language_evaluator = EasyLanguageEvaluator()
        df_sentence_level_results = pd.DataFrame()
        df_sentence_level_results = easy_language_evaluator.create_easy_language_results(preprocessed_text, title)
        df_sentence_level_results["Sentence"] = df_sentence_level_results["Sentence"].astype("str")
        df_sentence_level_results["Number of Satisfied Rules abs."] = df_sentence_level_results["Number of Satisfied Rules abs."].astype(int)
        df_sentence_level_results["Average Word Length (in Characters)"] = df_sentence_level_results["Average Word Length (in Characters)"].astype(float)
        # Zum Rounding-problem: "round" scheint schon zu funktionieren, allerdings müssten die hintersten 0 abgeschnitten werden ...
        #TODO: Einzelne Schritte als Erfolgreich anzeigen lassen.
        success = st.success("Evaluation successful!")
        if success:
            st.markdown("##### First glimpse on results")
            st.dataframe(df_sentence_level_results)
            st.write(df_sentence_level_results["Average Word Length (in Characters)"].dtypes)
