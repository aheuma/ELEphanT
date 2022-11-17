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
st.markdown("##### Insert title")
st.markdown("*Press enter to submit*")
title = st.text_input(label="title", label_visibility="collapsed")
if title:
    st.markdown("##### Insert text")
    #TODO: maximum text length
    st.info("Note: In submitting your text (pressing ctrl + enter) you agree that your text is preprocessed by ELEphanT. "
            "Preprocessing includes i.e. the substitution of french quotation marks (»«), which are commonly used in German literature, by German quotations („“).")
    st.markdown("*Press ctrl + enter to submit*")
    text = st.text_area(label="Insert your text", label_visibility="collapsed", height=350)
    if text and title:
        text_preprocessor = TextPreprocessor()
        preprocessed_text = text_preprocessor.preprocess_texts(text)
        success = st.success("Evaluation successfully completed!")
        if success:
            cb1 = st.checkbox("Display preprocessed text")
            if cb1:
                st.markdown(preprocessed_text)
            container1 = st.container()
            with container1:
                col1, col2, col3, col4 = st.columns([1,2,2,1])
                with col2:
                    btn2 = st.button("Sentence level results")
                with col3:
                    btn3 = st.button("Text level results")
                easy_language_evaluator = EasyLanguageEvaluator()
            if btn2:
                df_sentence_level_results = pd.DataFrame()
                df_sentence_level_results = easy_language_evaluator.create_easy_language_results(preprocessed_text, title)
                df_sentence_level_results["Sentence"] = df_sentence_level_results["Sentence"].astype("str")
                df_sentence_level_results["Number of Satisfied Rules abs."] = df_sentence_level_results["Number of Satisfied Rules abs."].astype(int)
                df_sentence_level_results["Average Word Length (in Characters)"] = df_sentence_level_results["Average Word Length (in Characters)"].astype(float)
                #Zum Rounding-problem: "round" scheint schon zu funktionieren, allerdings müssten die hintersten 0 abgeschnitten werden ...
                st.dataframe(df_sentence_level_results)
