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
    expander_sidebar_1 = st.sidebar.expander("Input & Specification")
    expander_sidebar_2 = st.sidebar.expander("Output – Results")
    with expander_sidebar_1:
        st.markdown("- **Preprocessing**: includes i.e. the substitution of french quotation marks (»«), "
                "which are commonly used in German literature, by German quotations („“).")
        st.markdown("- **Choseable Easy Language scores**: \n 1. Unweighted (default): Average number of fulfilled rules per text (in %)"
                    "\n 2. Weighted: Unweighted score is multiplied with average rule compliance scores from an Easy Language reference corpus (in %)"
                    "\n 3. Amount of perfect sentences: Percentage of sentences that fulfill at least 15 (of 16) rules (in %)")
        st.sidebar.image("./ELEphanT_logo.png", width=300)
    with expander_sidebar_2:
        st.markdown("**Three parts**: \n 1. Easy Language Score: Results depending on the chosen Easy Language score."
                    "\n 2. Rule Compliance: Overview over the most broken rules."
                    "\n 3. ELEphanT Output: Display preprocessed text and two-fold results: \n "
                    "- 3.1 Sentence level results, including the rule evaluations for every sentence. \n"
                    "\n - 3.2 Text level results, containing a summary of 3.1. \n - This output is always created und thus independent from the chosen evaluation mode.")

if "is_expanded" not in st.session_state:
    st.session_state["is_expanded"] = True

st.markdown("## ELEphanT: Analyze your Text")
expander_user_input = st.expander("Text input & evaluation mode specification", expanded=st.session_state["is_expanded"])
preprocessed_text = ""

# Form-like container to accept data from user
with expander_user_input:
    st.markdown("##### Chose Easy Language score")
    chosen_easy_language_score = st.radio("Pick one option", ("Unweighted", "Weighted", "Amount of perfect sentences"),
                                          help="Additional information on the scores can be found in the sidebar")
    st.markdown("##### Insert title")
    title = st.text_input(label="title", label_visibility="collapsed")
    st.markdown("*Press enter to submit*")
    st.markdown("##### Insert text")
    st.info("Recommended maximum text length: < 1.000.000 characters")
    text = st.text_area(label="Insert your text", label_visibility="collapsed", height=350)
    st.markdown("*Press ctrl + enter to submit and start ELEphanT*")
    text_preprocessor = TextPreprocessor()
    preprocessed_text = text_preprocessor.preprocess_texts(text)

# Print error if necessary data is missing
if not text and not title:
    st.error("Text and title are missing!")
elif not text:
    st.error("Text is missing!")
elif not title:
    st.error("Title is missing!")

# Precede with analysis only if all necessary data available
elif text and title:
    with st.spinner(text="ELEphanT is analyzing your text ..."):
        easy_language_evaluator = EasyLanguageEvaluator()
        dataframe_sentence_level_results = pd.DataFrame()
        dataframe_text_level_results = pd.DataFrame()
        dataframe_sentence_level_results, dataframe_text_level_results = easy_language_evaluator.create_easy_language_results(
            preprocessed_text, title)

        # text level dataframe modifications
        dataframe_text_level_results = dataframe_text_level_results.dropna()
        rules = ["High Numbers", "Percentage Numbers", "Written out Numbers", "Special Characters", "Repetitive Words",
                 "Long Words and Hyphens", "Abbreviations", "Nominalisations", "Passive Voice", "Genitive Case",
                 "Subjunctive Construct", "Negative Words", "Sentence Length", "Sentence Statements", "Complex Sentence Structure",
                 "Sentence Beginnings"]
        scores = []
        scores.append(dataframe_text_level_results.iat[0, 12] * 100)
        scores.append(dataframe_text_level_results.iat[0, 14] * 100)
        scores.append(dataframe_text_level_results.iat[0, 16] * 100)
        scores.append(dataframe_text_level_results.iat[0, 18] * 100)
        scores.append(dataframe_text_level_results.iat[0, 20] * 100)
        scores.append(dataframe_text_level_results.iat[0, 22] * 100)
        scores.append(dataframe_text_level_results.iat[0, 24] * 100)
        scores.append(dataframe_text_level_results.iat[0, 26] * 100)
        scores.append(dataframe_text_level_results.iat[0, 28] * 100)
        scores.append(dataframe_text_level_results.iat[0, 30] * 100)
        scores.append(dataframe_text_level_results.iat[0, 32] * 100)
        scores.append(dataframe_text_level_results.iat[0, 34] * 100)
        scores.append(dataframe_text_level_results.iat[0, 36] * 100)
        scores.append(dataframe_text_level_results.iat[0, 38] * 100)
        scores.append(dataframe_text_level_results.iat[0, 40] * 100)
        scores.append(dataframe_text_level_results.iat[0, 42] * 100)

        # create two modified dataframes on the basis of df_text_level_results
        dataframe_relative_text_level_results = pd.DataFrame({"Rule": rules, "Compliance Score": scores})
        dataframe_relative_text_level_results["Compliance Score"] = dataframe_relative_text_level_results["Compliance Score"].astype(int)

        dataframe_text_level_results_transposed = dataframe_text_level_results.T
        dataframe_text_level_results_transposed = dataframe_text_level_results_transposed.rename(index=str, columns={0: "Results"})

        # sentence level dataframe modifications
        dataframe_sentence_level_results["Sentence"] = dataframe_sentence_level_results["Sentence"].astype("str")
        dataframe_sentence_level_results["Number of Satisfied Rules abs."] = dataframe_sentence_level_results[
            "Number of Satisfied Rules abs."].astype(int)
        dataframe_sentence_level_results["Average Word Length (in Characters)"] = dataframe_sentence_level_results[
            "Average Word Length (in Characters)"].astype(float)
        dataframe_sentence_level_results = dataframe_sentence_level_results.sort_index()

        # Display Easy Language score results
        unweighted_easy_language_score = float(dataframe_text_level_results.iat[0, 7])
        weighted_easy_language_score = float(dataframe_text_level_results.iat[0, 8])
        perfect_sentences_score = dataframe_text_level_results.iat[0, 10]
        perfect_sentences_abs = dataframe_text_level_results.iat[0, 9]
        number_of_sentences = dataframe_text_level_results.iat[0, 1]

        # first things to be displayed after evaluation
        st.markdown("## Output – Results")
        tab_easy_language_score, tab_rule_compliance, tab_elephant_output = st.tabs(["Easy Language Score", "Rule Compliance", "ELEphanT Output"])

        with tab_easy_language_score:
            if chosen_easy_language_score == "Unweighted":
                if unweighted_easy_language_score >= 0.5:
                    st.markdown(f"# 🎉 {unweighted_easy_language_score} 🎉")
                else:
                    st.markdown(f"# {unweighted_easy_language_score}")
                st.markdown(f"### Your text complies with the rules of Easy Language to {'{:.1%}'.format(unweighted_easy_language_score)}.")
            elif chosen_easy_language_score == "Weighted":
                if weighted_easy_language_score >= 0.5:
                    st.markdown(f"# 🎉 {weighted_easy_language_score} 🎉")
                else:
                    st.markdown(f"# {weighted_easy_language_score}")
                st.markdown(
                    f"### Your text complies with the rules of Easy Language to {'{:.1%}'.format(weighted_easy_language_score)}.")
            elif chosen_easy_language_score == "Amount of perfect sentences":
                if perfect_sentences_score > 0.02:
                    st.markdown(f"# 🎉 {perfect_sentences_score} 🎉")
                else:
                    st.markdown(f"# {perfect_sentences_score}")
                if perfect_sentences_abs == 1:
                    st.markdown(
                        f"### {perfect_sentences_abs} of {number_of_sentences} sentences in the text complies to at least 15 rules.")
                else:
                    st.markdown(f"### {perfect_sentences_abs} of {number_of_sentences} sentences in the text comply to at least 15 rules.")
                st.markdown(
                    f"### This corresponds to {'{:.1%}'.format(perfect_sentences_score)}.")

            #TODO: only show the chosen EL score here?
            # Display Easy Language reference scores in an expander
            expander_reference_scores = st.expander("Reference Scores", expanded=True)
            with expander_reference_scores:
                tab_easy_language_reference_texts, tab_standard_german_reference_texts = st.tabs(["Easy Language Texts", "Standard German Texts"])
                with tab_easy_language_reference_texts:
                    dataframe_reference_easy_language = pd.read_excel("./Easy_Language_Reference_Texts.xlsx")
                    st.dataframe(dataframe_reference_easy_language)
                with tab_standard_german_reference_texts:
                    dataframe_reference_standard_german = pd.read_excel("./Standard_German_Reference_Texts.xlsx")
                    st.dataframe(dataframe_reference_standard_german)
                st.write("*For more information on the reference texts' sources, cf. with [Information on Research Project](http://localhost:8501/Information_on_Research_Project).*")

        with tab_rule_compliance:
            # Rule compliance: table and graph
            tab_tabular_rule_scores, tab_graph_visualization = st.tabs(["Tabular Rule Scores", "Graph Visualization"])
            with tab_tabular_rule_scores:
                st.dataframe(dataframe_relative_text_level_results)
            with tab_graph_visualization:
                # Create result plot
                plt.style.use("ggplot")
                x_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
                plt.bar(x_pos, scores, color="steelblue")
                plt.title("Rule Compliance in %")
                plt.xticks(x_pos, rules)
                plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment="right")
                st.pyplot(plt)
        with tab_elephant_output:
            # Further ELEphanT results (preprocessed text and excel sheets)
            expander_preprocessed_text = st.expander("Preprocessed text", expanded=True)
            expander_sentence_level_results = st.expander("Sentence level results")
            expander_text_level_results = st.expander("Text level results")
            with expander_preprocessed_text:
                st.markdown(preprocessed_text)
            with expander_sentence_level_results:
                st.dataframe(dataframe_sentence_level_results)
            with expander_text_level_results:
                st.dataframe(dataframe_text_level_results_transposed, width=120)
