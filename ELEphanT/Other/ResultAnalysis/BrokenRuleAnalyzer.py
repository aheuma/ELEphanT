import pandas as pd


class BrokenRuleAnalyzer:

    def __init__(self, file_text_level_xlsx_results):
        self.df_text_level = pd.read_excel(file_text_level_xlsx_results)

    def return_most_broken_rules_text_level(self):
        ranked_most_broken_rules_dict = {}
        rule_names = ["R1: High Numbers", "R2: Percentage Numbers", "R3: Written out Numbers", "R4: Special Characters",
                      "R5: Repetitive Words", "R6: Long Words and Hyphens", "R7: Abbreviations",
                      "R8: Nominalisations", "R9: Passive Voice", "R10: Genitive Case", "R11: Subjunctive Construct",
                      "R12: Negative Words", "R13: Long Sentence", "R14: Multiple Sentence Statements",
                      "R15: Complex Sentence Structure", "R16: Sentence Beginnings"]
        tmp_df = self.df_text_level.iloc[:, [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42]]
        rule_results_rel = round(tmp_df.mean(), 3)
        rule_results_rel = rule_results_rel.tolist()
        for key in rule_names:
            for value in rule_results_rel:
                ranked_most_broken_rules_dict[key] = value
                rule_results_rel.remove(value)
                break
        ranked_most_broken_rules_tuples = sorted(ranked_most_broken_rules_dict.items(), key=lambda item: item[1])
        return ranked_most_broken_rules_tuples
