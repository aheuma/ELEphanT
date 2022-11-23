import lamda as lamda
import numpy as np
import streamlit as st
import sys
sys.path.append("./PreProcessing/")
sys.path.append("./Model/")
from TextPreprocessor import TextPreprocessor
from EasyLanguageEvaluator import EasyLanguageEvaluator
import pandas as pd

st.set_page_config(layout="wide")
title_alignment = """
<style>
#the-title {
text-align: center
}
</style>
"""

sidebar = st.sidebar
with sidebar:
    st.markdown("## Additional information")
    exp1 = st.sidebar.expander("Input & Specification")
    exp2 = st.sidebar.expander("Output – Results")
    with exp1:
        st.markdown("- **Preprocessing**: includes i.e. the substitution of french quotation marks (»«), "
                "which are commonly used in German literature, by German quotations („“).")
        st.markdown("- **Choseable evaluation modes**: \n 1. Easy Language rules only (default) \n 2. Easy "
                    "Language rules and additional text characteristics (i.e. number of tokens or words per sentence).")
        st.markdown("- **Choseable Easy Language scores**: \n 1. Unweighted (default): Average number of fulfilled rules per text (in %)"
                    "\n 2. Weighted: Unweighted score is multiplied with average rule compliance scores from an Easy Language reference corpus (in %)"
                    "\n 3. Amount of perfect sentences: Percentage of sentences that fulfill at least 15 (of 16) rules (in %)")
        st.sidebar.image("./ELEphanT_logo.png", width=300)
    with exp2:
        st.markdown("- **Two kinds of results**: \n 1. Sentence level results, including the rule evaluations for every sentence."
                    "\n 2. Text level results, containing a summary of 1. \n This output is always created und thus independent from the chosen evaluation mode.")

st.markdown("## ELEphanT: Analyze your Text")
if "is_expanded" not in st.session_state:
    st.session_state["is_expanded"] = True
exp3 = st.expander("Text input & evaluation mode specification", expanded=st.session_state["is_expanded"])
preprocessed_text = ""
with exp3:
    st.markdown("##### Insert title")
    title = st.text_input(label="title", label_visibility="collapsed")
    st.markdown("*Press enter to submit*")
    st.markdown("##### Insert text")
    # TODO: maximum text length
    st.markdown("*Press ctrl + enter to submit*")
    text = st.text_area(label="Insert your text", label_visibility="collapsed", height=350)
    text_preprocessor = TextPreprocessor()
    preprocessed_text = text_preprocessor.preprocess_texts(text)
    st.markdown("##### Chose evaluation mode")
    chosen_evaluation_mode = st.radio("Pick one", ("Easy Language rules only", "Easy Language rules and text characteristics"),
                                           label_visibility="collapsed")
    st.markdown("##### Chose Easy Language score")
    chosen_easy_language_score = st.radio("Pick one", ("Unweighted", "Weighted", "Amount of perfect sentences"),
                               label_visibility="collapsed")
if not text or not title:
    st.error("Insert your data!")
elif text and title:
    #st.session_state["is_expanded"] = False
    #TODO: enable expander collapsing here?
    st.markdown("## Output – Results")

    easy_language_evaluator = EasyLanguageEvaluator()
    df_sentence_level_results = pd.DataFrame()
    df_text_level_results = pd.DataFrame()

    df_sentence_level_results, df_text_level_results = easy_language_evaluator.create_easy_language_results(
        preprocessed_text, title)
    # text level dataframe modifications
    df_text_level_results = df_text_level_results.dropna()
    df_text_level_results = df_text_level_results.T
    df_text_level_results = df_text_level_results.rename(index=str, columns={0: "Results"})

    # sentence level dataframe modifications
    df_sentence_level_results["Sentence"] = df_sentence_level_results["Sentence"].astype("str")
    df_sentence_level_results["Number of Satisfied Rules abs."] = df_sentence_level_results[
        "Number of Satisfied Rules abs."].astype(int)
    df_sentence_level_results["Average Word Length (in Characters)"] = df_sentence_level_results[
        "Average Word Length (in Characters)"].astype(float)
    # Zum Rounding-problem: "round" scheint schon zu funktionieren, allerdings müssten die hintersten 0 abgeschnitten werden ...
    df_sentence_level_results = df_sentence_level_results.sort_index()

    # TODO: Insert evaluation Mode
    if chosen_evaluation_mode == "Easy Language rules only":
        pass
    elif chosen_evaluation_mode == "Easy Language rules and text characteristics":
        pass

    # TODO: Grafik

    if chosen_easy_language_score == "Unweighted":
        unweighted_score = float(df_text_level_results.iat[7, 0])
        st.markdown(f"**Unweighted Easy Language score: {unweighted_score}**")
        st.markdown(f"### Your text complies with the rules of Easy Language to {'{:.1%}'.format(unweighted_score)}")
    elif chosen_easy_language_score == "Weighted":
        weighted_score = float(df_text_level_results.iat[8, 0])
        st.markdown(f"**Weighted Easy Language score: {weighted_score}**")
        st.markdown(
                f"### Your text complies with the rules of Easy Language to {'{:.1%}'.format(weighted_score)}")
    elif chosen_easy_language_score == "Amount of perfect sentences":
        perfect_sentences_score = df_text_level_results.iat[10, 0]
        st.markdown(f"**Unweighted Easy Language score: {perfect_sentences_score}**")
        st.markdown(f"### {'{:.1%}'.format(perfect_sentences_score)} of the text's sentences comply at least to 15 rules")
    exp4 = st.expander("Preprocessed text")
    exp5 = st.expander("Sentence level results")
    exp6 = st.expander("Text level results", expanded=True)
    with exp4:
        st.markdown(preprocessed_text)
    with exp5:
       st.dataframe(df_sentence_level_results)
    with exp6:
        st.table(df_text_level_results)

    # Possible extensions
    # Create graph with all sentences on y-axis and number of fulfilled rules on x-axis