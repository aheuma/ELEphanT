import streamlit as st
import sys
sys.path.append("./PreProcessing/")
sys.path.append("./Model/")
from TextPreprocessor import TextPreprocessor
from EasyLanguageEvaluator import EasyLanguageEvaluator
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# Create sidebar with additional information
sidebar = st.sidebar
with sidebar:
    st.markdown("## Additional information")
    exp1 = st.sidebar.expander("Input & Specification")
    exp2 = st.sidebar.expander("Output – Results")
    with exp1:
        st.markdown("- **Preprocessing**: includes i.e. the substitution of french quotation marks (»«), "
                "which are commonly used in German literature, by German quotations („“).")
        st.markdown("- **Choseable Easy Language scores**: \n 1. Unweighted (default): Average number of fulfilled rules per text (in %)"
                    "\n 2. Weighted: Unweighted score is multiplied with average rule compliance scores from an Easy Language reference corpus (in %)"
                    "\n 3. Amount of perfect sentences: Percentage of sentences that fulfill at least 15 (of 16) rules (in %)")
        st.sidebar.image("./ELEphanT_logo.png", width=300)
    with exp2:
        st.markdown("- **Two kinds of results**: \n 1. Sentence level results, including the rule evaluations for every sentence."
                    "\n 2. Text level results, containing a summary of 1. \n This output is always created und thus independent from the chosen evaluation mode.")

if "is_expanded" not in st.session_state:
    st.session_state["is_expanded"] = True

st.markdown("## ELEphanT: Analyze your Text")
exp3 = st.expander("Text input & evaluation mode specification", expanded=st.session_state["is_expanded"])
preprocessed_text = ""

# Form-like container to accept inserted data from user
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
    st.markdown("##### Chose Easy Language score")
    chosen_easy_language_score = st.radio("Pick one", ("Unweighted", "Weighted", "Amount of perfect sentences"),
                               label_visibility="collapsed")

# Print error if necessary data is missing
if not text or not title:
    st.error("Insert your data!")

# Precede with analysis only if all necessary data available
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
    rules = ["High Numbers", "Percentage Numbers", "Written out Numbers", "Special Characters", "Repetitive Words",
             "Long Words and Hyphens", "Abbreviations", "Nominalisations", "Passive Voice", "Genitive Case",
             "Subjunctive Construct", "Negative Words", "Sentence Length", "Sentence Statements", "Complex Sentence Structure",
             "Sentence Beginnings"]
    scores = []
    scores.append(df_text_level_results.iat[0, 12]*100)
    scores.append(df_text_level_results.iat[0, 14]*100)
    scores.append(df_text_level_results.iat[0, 16]*100)
    scores.append(df_text_level_results.iat[0, 18]*100)
    scores.append(df_text_level_results.iat[0, 20]*100)
    scores.append(df_text_level_results.iat[0, 22]*100)
    scores.append(df_text_level_results.iat[0, 24]*100)
    scores.append(df_text_level_results.iat[0, 26]*100)
    scores.append(df_text_level_results.iat[0, 28]*100)
    scores.append(df_text_level_results.iat[0, 30]*100)
    scores.append(df_text_level_results.iat[0, 32]*100)
    scores.append(df_text_level_results.iat[0, 34]*100)
    scores.append(df_text_level_results.iat[0, 36]*100)
    scores.append(df_text_level_results.iat[0, 38]*100)
    scores.append(df_text_level_results.iat[0, 40]*100)
    scores.append(df_text_level_results.iat[0, 42]*100)
    #scores = df_text_level_results.iloc[:, [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]]

    df_rel_text_level_results = pd.DataFrame({"Rule": rules, "Compliance Score": scores})
    df_rel_text_level_results["Compliance Score"] = df_rel_text_level_results["Compliance Score"].astype(int)

    df_text_level_results_transposed = df_text_level_results.T
    df_text_level_results_transposed = df_text_level_results_transposed.rename(index=str, columns={0: "Results"})

    # sentence level dataframe modifications
    df_sentence_level_results["Sentence"] = df_sentence_level_results["Sentence"].astype("str")
    df_sentence_level_results["Number of Satisfied Rules abs."] = df_sentence_level_results[
        "Number of Satisfied Rules abs."].astype(int)
    df_sentence_level_results["Average Word Length (in Characters)"] = df_sentence_level_results[
        "Average Word Length (in Characters)"].astype(float)
    # Zum Rounding-problem: "round" scheint schon zu funktionieren, allerdings müssten die hintersten 0 abgeschnitten werden ...
    df_sentence_level_results = df_sentence_level_results.sort_index()

    col1, col2 = st. columns(2)
    with col1:
        st.dataframe(df_rel_text_level_results)
        # Different Easy Language score outcome
        if chosen_easy_language_score == "Unweighted":
            unweighted_score = float(df_text_level_results.iat[0, 7])
            st.markdown(f"**Unweighted Easy Language score: {unweighted_score}**")
        elif chosen_easy_language_score == "Weighted":
            weighted_score = float(df_text_level_results.iat[0, 8])
            st.markdown(f"### Weighted Easy Language score: {weighted_score}")
        elif chosen_easy_language_score == "Amount of perfect sentences":
            perfect_sentences_score = df_text_level_results.iat[0, 10]
            st.markdown(f"### Unweighted Easy Language score: {perfect_sentences_score}")

    with col2:
        # Different Easy Language score outcome
        if chosen_easy_language_score == "Unweighted":
            st.markdown(
                f"#### Your text complies with the rules of Easy Language to {'{:.1%}'.format(unweighted_score)}")
        elif chosen_easy_language_score == "Weighted":
            st.markdown(
                f"### Your text complies with the rules of Easy Language to {'{:.1%}'.format(weighted_score)}")
        elif chosen_easy_language_score == "Amount of perfect sentences":
            st.markdown(
                f"### {'{:.1%}'.format(perfect_sentences_score)} of the text's sentences comply at least to 15 rules")
        #TODO: Easy Language compliance score mehr hervorheben
    # Create result plot
    plt.style.use("ggplot")
    x_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    plt.bar(x_pos, scores, color="steelblue")
    plt.title("Rule Compliance in %")
    plt.xticks(x_pos, rules)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment="right")
    st.pyplot(plt)


    exp4 = st.expander("Preprocessed text")
    exp5 = st.expander("Sentence level results")
    exp6 = st.expander("Text level results", expanded=True)
    with exp4:
        st.markdown(preprocessed_text)
    with exp5:
       st.dataframe(df_sentence_level_results)
    with exp6:
        st.dataframe(df_text_level_results)
