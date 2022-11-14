import os
import spacy
from spacy import Language
from Model.ExcelSheetCreator import ExcelSheetCreator
from Model.SentenceLevelResults import SentenceLevelResults
from Model.TextLevelResults import TextLevelResults


class EasyLanguageEvaluator:

    def __init__(self, path_to_txt_files, path_sentence_level_xlsx_results, text_level_xlsx_results):
        self.path_to_txt_files = path_to_txt_files
        self.path_sentence_level_xlsx_results = path_sentence_level_xlsx_results
        self.text_level_xlsx_results = text_level_xlsx_results
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

    def create_easy_language_results(self):
        excel_sheet_creator = ExcelSheetCreator()
        excel_sheet_creator.create_text_level_results(self.text_level_xlsx_results)
        row_counter = 0
        for file in os.listdir(self.path_to_txt_files):
            if file.endswith(".txt"):
                with open(self.path_to_txt_files / file, "r") as f:
                    print(f"Evaluating Easy Language in file {file}")
                    file_contents = f.read()
                    doc = self.nlp(file_contents)

                    # create filename without appendix and slashes
                    filename = self.path_to_txt_files / file
                    filename_txt = filename.name
                    filename_without_extension = filename.stem
                    new_filename = filename_without_extension + "_sentence_results.xlsx"

                    # create sentence level excel file
                    sentence_level_xlsx_results = self.path_sentence_level_xlsx_results / new_filename
                    excel_sheet_creator.create_sentence_level_results(sentence_level_xlsx_results)

                    # create results on sentence level
                    results_on_sentence_level_creator = SentenceLevelResults()
                    results_on_sentence_level_creator.analyse_text_on_sentence_level(doc, filename_txt, self.nlp, sentence_level_xlsx_results)

                    # create results on text level
                    results_on_text_level_creator = TextLevelResults(sentence_level_xlsx_results)
                    results_on_text_level_creator.analyse_text_on_text_level(self.text_level_xlsx_results, row_counter)
                    row_counter += 1
