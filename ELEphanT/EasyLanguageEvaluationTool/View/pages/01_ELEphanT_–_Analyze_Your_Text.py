import streamlit as st
#from EasyLanguageTool.SentenceLevelResults import SentenceLevelResults
#from EasyLanguageTool.TextLevelResults import TextLevelResults

st.sidebar.image("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Logo/ELEphanT_logo.png", width=300)


st.markdown("## ELEphanT: Analyze your Text")

exp1 = st.expander("1. Text Input", expanded=True)
exp2 = st.expander("2. Pre-Processing")
exp3 = st.expander("3. Sentence Level Analysis")
exp4 = st.expander("4. Text Level Analysis")

with exp1:
    st.markdown("##### Paste the title of your text")
    title = st.text_input(label="title", label_visibility="collapsed")
    st.markdown("##### Paste your text")
    text = st.text_area(label="Insert your text", label_visibility="collapsed", height=350)
    if text and not title:
        st.error("You forgot to add the title.")
    elif title and not text:
        st.info("Please insert your text now.")
    elif text and title:
        st.success("All necessary data has been pasted. You can now move on to the next step.")
if text and title:
    with exp2: #TODO: das hier nicht als extra Schritt machen, sondern einfach HInweis einbauen, dass der Text für die Evaluation auch preprocessed wird. Dann mit Button Klick direkt Ergebnis bringen.
        st.info("Note: This tool works best when your text has undergone some cleaning operations (pre-processing). "
            "For example: French quotation marks (»«), which are commonly used in German literature, should be replaced by German quotations („“). "
            "Using the tool without applying the pre-processing option is therefore not allowed.")
        btn = st.button("Read and accepted!")
        if btn:
            # TODO: Hier: Aufruf Preprocessing-Klasse. Weitergabe des Hier eingegebenen Textes und Rücknahme des bereinigten Textes
            # TODO: Exception Handling, falls was schiefgeht?!
            st.success("Great, the pre-processing was successful. You can now move on to the next step.")
            with exp3:
                st.markdown("##### First glimpse on results")
                # TODO: display df.head()
                # TODO: download button, um excel-tabelle herunterzuladen.
