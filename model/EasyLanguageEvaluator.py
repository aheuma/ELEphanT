import spacy
from spacy import Language
from SentenceLevelResults import SentenceLevelResults
from TextLevelResults import TextLevelResults


class EasyLanguageEvaluator:

    def __init__(self):
        self.nlp = spacy.load("de_core_news_sm")

        # Modifying spacy sentence boundaries
        @Language.component("set_custom_boundaries")
        def set_custom_boundaries(doc):
            for token in doc[:-1]:
                if token.text == ";":
                    doc[token.i + 1].is_sent_start = False
                elif token.text == "„":
                    doc[token.i + 1].is_sent_start = False
                elif token.text == ":":
                    doc[token.i + 1].is_sent_start = False
                elif token.text == "‚":
                    doc[token.i + 1].is_sent_start = False
            return doc

        self.nlp.add_pipe("set_custom_boundaries", before="parser")

    def create_easy_language_results(self, preprocessed_text, title):
        doc = self.nlp(preprocessed_text)

        # create results on sentence level
        results_on_sentence_level_creator = SentenceLevelResults()
        df_sentence_level_results = results_on_sentence_level_creator.analyse_text_on_sentence_level(doc, title, self.nlp)

        # create results on text level
        results_on_text_level_creator = TextLevelResults(df_sentence_level_results)
        df_text_level_results = results_on_text_level_creator.analyse_text_on_text_level()
        return df_sentence_level_results, df_text_level_results
