import os
import textstat

class ReadabilityMetricsAnalyzer:

    def __init__(self, directory_preprocessed_txt_files):
        self.directory_preprocessed_txt_files = directory_preprocessed_txt_files
        textstat.set_lang("de")


    def calculate_readability_score(self):
        wiener_sachtextformel = []
        flesch_kincaid = []
        flesch_reading_ease = []
        for file in os.listdir(self.directory_preprocessed_txt_files):
            if file.endswith(".txt"):
                with open(self.directory_preprocessed_txt_files + file, "r") as f:
                    file_contents = f.read()
                    wiener_sachtextformel.append(textstat.wiener_sachtextformel(file_contents, 4))
                    flesch_kincaid.append(textstat.flesch_kincaid_grade(file_contents))
                    flesch_reading_ease.append(textstat.flesch_reading_ease(file_contents))
                    #print(file, textstat.flesch_kincaid_grade(file_contents))
                    #print(file, textstat.flesch_reading_ease(file_contents))
                    #print(file, textstat.wiener_sachtextformel(file_contents, 4))
        return wiener_sachtextformel
        #flesch_reading_ease = textstat.flesch_reading_ease(text)
        #flesch_kincaid_grade = textstat.flesch_kincaid_grade(text)
