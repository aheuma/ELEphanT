from Model.EasyLanguageEvaluator import EasyLanguageEvaluator
from PreProcessing.TextPreprocessor import TextPreprocessor
from pathlib import Path

''' Note: this tool will analyze all txt.-files in the given directory
1. You will insert your original text file(s); the tool will do some preprocessing and save the processed files in a new folder.
2. On the basis of the preprocessed files: Each text file is analyzed in terms of Easy Language. 
An excel file with all results on sentence level is created for each text file.
3. A summarizing excel file is created on the basis of the sentence level excel file(s).
'''

directory_original_txt_files = Path("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Evaluation/Wilde_Jana/")
directory_preprocessed_txt_files = Path("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Evaluation/Wilde_Jana/preprocessed/")
directory_sentence_level_xlsx_results = Path("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Evaluation/Wilde_Jana/Results/")
resultname = "Text_Level_Results.xlsx"
file_text_level_xlsx_results = directory_sentence_level_xlsx_results / resultname

# Text preprocessing
print("Preprocess texts ...")
text_preprocessor = TextPreprocessor(directory_original_txt_files, directory_preprocessed_txt_files)
text_preprocessor.preprocess_texts()
print("Preprocessing successful!")

# Evaluation of the text's degree of Easy Language
print("Evaluating Easy Language ...")
easy_language_evaluator = EasyLanguageEvaluator(directory_preprocessed_txt_files, directory_sentence_level_xlsx_results, file_text_level_xlsx_results)
easy_language_evaluator.create_easy_language_results()
print("Evaluation successful!")
