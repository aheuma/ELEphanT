import pandas as pd


class ExcelSheetCreator:

    def __init__(self):
        pass

    # Creates excel files for each text file (no rows, only columns)
    def create_sentence_level_results(self, path_to_sentence_level_results):
        df_sentence_level_results = pd.DataFrame(
            columns=["Filename", "Sentence", "Sentence Number", "Tokens per Sentence", "Words per Sentence", "Average Word Length (in Characters)",
                     "Characters per Sentence", "R1: High Numbers", "R2: Percentage Numbers", "R3: Written out Numbers",
                     "R4: Special Characters", "R5: Repetitive Words", "R6: Long Words", "R6: Long Words without Hyphens",
                     "R6: Sum: Long Words and Hyphens",
                     "R7: Abbreviations", "R8: Nominalisations", "R9: Passive Voice", "R10: Genitive Case",
                     "R11: Subjunctive Construct", "R12: Negative Words", "R13: Long Sentence",
                     "R14: Multiple Sentence Statements", "R15: Complex Sentence Structure", "R16: Sentence Beginnings"], index=[1])
        writer = pd.ExcelWriter(path_to_sentence_level_results, engine="xlsxwriter")
        df_sentence_level_results.to_excel(writer, sheet_name="Results", index=False)
        writer.close()

    # Creates the final excel file (no rows, only columns)
    def create_text_level_results(self, path_to_text_level_results):
        df_text_level_results = pd.DataFrame(
            columns=["Filename", "Number of Sentences per Text", "Number of Tokens per Text", "Number of Words per Text",
                     "Average Sentence Length (in Words)", "Number of Characters per Text",
                     "Average Number of Satisfied Rules abs. (unweighted)",
                     "Unweighted Easy Language Score (in %) \n (Average Amount of Satisfied Rules (in %))",
                     "Weighted Easy Language Score (in %)", "Number of Perfect Sentences per Text abs.",
                     "Amount of Perfect Sentences per Text (in %)", "R1: High Numbers (abs.)", "R1: High Numbers (in %)",
                     "R2: Percentage Numbers (abs.)", "R2: Percentage Numbers (in %)", "R3: Written out Numbers (abs.)",
                     "R3: Written out Numbers (in %)", "R4: Special Characters (abs.)", "R4: Special Characters (in %)",
                     "R5: Repetitive Words (abs.)", "R5: Repetitive Words (in %)", "R6: Long Words and Hyphens (abs.)",
                     "R6: Long Words and Hyphens (in %)", "R7: Abbreviations (abs.)", "R7: Abbreviations (in %)",
                     "R8: Nominalisations (abs.)", "R8: Nominalisations (in %)", "R9: Passive Voice (abs.)",
                     "R9: Passive Voice (in %)", "R10: Genitive Case (abs.)", "R10: Genitive Case (in %)",
                     "R11: Subjunctive Construct (abs.)", "R11: Subjunctive Construct (in %)",
                     "R12: Negative Words (abs.)", "R12: Negative Words (in %)", "R13: Sentence Length (abs.)",
                     "R13: Sentence Length (in %)", "R14: Sentence Statements (abs.)", "R14: Sentence Statements (in %)",
                     "R15: Complex Sentence Structure (abs.)", "R15: Complex Sentence Structure (in %)",
                     "R16: Sentence Beginnings (abs.)", "R16: Sentence Beginnings (in %)"], index=[1])
        writer = pd.ExcelWriter(path_to_text_level_results, engine="xlsxwriter")
        df_text_level_results.to_excel(writer, sheet_name="Results", index=False)
        writer.close()
