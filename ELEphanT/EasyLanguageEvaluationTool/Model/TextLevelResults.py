import pandas as pd


class TextLevelResults:

    def __init__(self, input_excel_file):
        self.df = pd.read_excel(input_excel_file)
        self.only_rules_df = self.df.iloc[:, [9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]]

    def sum_sentence_level_results(self):
        sents_without_broken_rule_abs = []
        sents_without_broken_rule_rel = []
        for column in self.only_rules_df:
            sents_without_broken_rule_abs.append(len(self.only_rules_df.loc[self.only_rules_df[column] == 1]))
        for number in sents_without_broken_rule_abs:
            percentage_number = round((number / len(self.only_rules_df)), 3)
            sents_without_broken_rule_rel.append(percentage_number)
        return sents_without_broken_rule_abs, sents_without_broken_rule_rel

    def sum_text_characteristics(self):
        filename = self.df["Filename"][0]
        number_of_sentences = len(self.df)
        average_sentence_length = round(self.df["Words per Sentence"].mean(), 3)
        number_of_tokens = self.df["Tokens per Sentence"].sum()
        number_of_words = self.df["Words per Sentence"].sum()
        number_of_characters = self.df["Characters per Sentence"].sum()
        all_text_characteristics = [filename, number_of_sentences, number_of_tokens, number_of_words, average_sentence_length, number_of_characters]
        return all_text_characteristics

    def calculate_weighted_el_score_rel(self):
        all_weighted_rules = [self.df["R1: High Numbers"].mean() * 1.000, self.df["R2: Percentage Numbers"].mean() * 1.000,
                                  self.df["R3: Written out Numbers"].mean() * 0.997, self.df["R4: Special Characters"].mean() * 0.990,
                                  self.df["R5: Repetitive Words"].mean() * 0.977, self.df["R6: Sum: Long Words and Hyphens"].mean() * 0.670,
                                  self.df["R7: Abbreviations"].mean() * 1.000, self.df["R8: Nominalisations"].mean() * 0.896,
                                  self.df["R9: Passive Voice"].mean() * 0.957, self.df["R10: Genitive Case"].mean() * 0.954,
                                  self.df["R11: Subjunctive Construct"].mean() * 0.998, self.df["R12: Negative Words"].mean() * 0.937,
                                  self.df["R13: Long Sentence"].mean() * 0.666, self.df["R14: Multiple Sentence Statements"].mean() * 0.921,
                                  self.df["R15: Complex Sentence Structure"].mean() * 0.335, self.df["R16: Sentence Beginnings"].mean() * 0.084]
        return round(((sum(all_weighted_rules) / len(all_weighted_rules))), 3)

    def safe_results_in_excel_file(self, text_characteristics_results, rule_results_abs, rule_results_rel,
                                   path_to_text_level_results, counter):
        df = pd.read_excel(path_to_text_level_results)
        tmp_df2 = self.df.iloc[:, 7]
        average_satisfied_rules_abs = round(tmp_df2.mean(), 3)
        average_satisfied_rules_rel = round((average_satisfied_rules_abs / len(self.only_rules_df.columns)), 3)
        weighted_easy_language_score_rel = self.calculate_weighted_el_score_rel()
        number_of_perfect_sentences_abs = (self.df["Number of Satisfied Rules abs."] >= 15).sum() # perfect sent = max. 1 broken rule
        number_of_perfect_sentences_rel = round((number_of_perfect_sentences_abs / len(tmp_df2)), 3)
        new_data_row = [text_characteristics_results[0], text_characteristics_results[1], text_characteristics_results[2],
                        text_characteristics_results[3], text_characteristics_results[4], text_characteristics_results[5],
                        average_satisfied_rules_abs, average_satisfied_rules_rel, weighted_easy_language_score_rel, number_of_perfect_sentences_abs,
                        number_of_perfect_sentences_rel, rule_results_abs[0], rule_results_rel[0], rule_results_abs[1],
                        rule_results_rel[1], rule_results_abs[2], rule_results_rel[2], rule_results_abs[3],
                        rule_results_rel[3], rule_results_abs[4], rule_results_rel[4], rule_results_abs[5], rule_results_rel[5],
                        rule_results_abs[6], rule_results_rel[6], rule_results_abs[7], rule_results_rel[7], rule_results_abs[8],
                        rule_results_rel[8], rule_results_abs[9], rule_results_rel[9], rule_results_abs[10], rule_results_rel[10],
                        rule_results_abs[11], rule_results_rel[11], rule_results_abs[12], rule_results_rel[12],
                        rule_results_abs[13], rule_results_rel[13], rule_results_abs[14], rule_results_rel[14], rule_results_abs[15],
                        rule_results_rel[15]]
        df.loc[counter] = new_data_row
        writer = pd.ExcelWriter(path_to_text_level_results, engine="xlsxwriter")
        df.to_excel(writer, sheet_name="Results", index=False)
        writer.close()

    def analyse_text_on_text_level(self, path_to_text_level_results, counter):
        text_characteristics_results = self.sum_text_characteristics()
        rule_results_abs, rule_results_rel = self.sum_sentence_level_results()
        self.safe_results_in_excel_file(text_characteristics_results, rule_results_abs, rule_results_rel,
                                        path_to_text_level_results, counter)
