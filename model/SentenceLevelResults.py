import pandas as pd
from CharacterRuleEvaluator import CharacterRuleEvaluator
from TextCharacteristicsEvaluator import TextEvaluator
from WordRuleEvaluator import WordRuleEvaluator
from SentenceRuleEvaluator import SentenceRuleEvaluator

class SentenceLevelResults:

    def __init__(self):
        self.sentence_evaluator = SentenceRuleEvaluator()
        self.character_evaluator = CharacterRuleEvaluator()
        self.word_evaluator = WordRuleEvaluator()
        self.text_characteristic_evaluator = TextEvaluator()

    def evaluate_Leichte_Sprache_rules(self, doc, nlp):
        high_numbers, percentage_numbers, written_out_numbers, special_characters = self.character_evaluator.evaluate(doc)
        word_repetitions, long_words, hyphens_in_words, abbreviations, nominalisations, passive_constructs, genitive_constructs, subjunctive_constructs, negative_constructs = self.word_evaluator.evaluate(doc, nlp)
        long_sentences, multiple_statements, complex_sentences, allowed_sentence_beginnings = self.sentence_evaluator.evaluate(doc, nlp)
        sum_long_words_hyphens = []
        for i, j in zip(long_words, hyphens_in_words):
            if i == 1:
                # no long word at all –> good
                sum_long_words_hyphens.append(1)
            elif i == 0 and j == 1:
                # long word with hyphen –> good
                sum_long_words_hyphens.append(1)
            elif i == 0 and j == 0:
                # long word, but no hyphen –> bad
                sum_long_words_hyphens.append(0)
            else:
                # 0 1 = actually not existent
                sum_long_words_hyphens.append(1)
        all_rule_results = [high_numbers, percentage_numbers, written_out_numbers, special_characters, word_repetitions,
                            long_words, hyphens_in_words, sum_long_words_hyphens, abbreviations, nominalisations,
                            passive_constructs, genitive_constructs, subjunctive_constructs, negative_constructs,
                            long_sentences, multiple_statements, complex_sentences, allowed_sentence_beginnings]
        return all_rule_results

    def evaluate_text_characteristics(self, doc, title):
        titles, sentences, sentence_numbers, sentence_length_tokens, sentence_length_words, average_word_length, sentence_length_characters = self.text_characteristic_evaluator.evaluate(doc, title)
        all_text_characteristics = [titles, sentences, sentence_numbers, sentence_length_tokens, sentence_length_words, average_word_length, sentence_length_characters]
        return all_text_characteristics

    def create_sentence_level_df(self, text_characteristics, easy_language_rules):
        df_sentence_level_results = pd.DataFrame(
            columns=["Title", "Sentence", "Sentence Number", "Tokens per Sentence", "Words per Sentence",
                     "Average Word Length (in Characters)",
                     "Characters per Sentence", "R1: High Numbers", "R2: Percentage Numbers", "R3: Written out Numbers",
                     "R4: Special Characters", "R5: Repetitive Words", "R6: Long Words",
                     "R6: Long Words without Hyphens",
                     "R6: Sum: Long Words and Hyphens",
                     "R7: Abbreviations", "R8: Nominalisations", "R9: Passive Voice", "R10: Genitive Case",
                     "R11: Subjunctive Construct", "R12: Negative Words", "R13: Long Sentence",
                     "R14: Multiple Sentence Statements", "R15: Complex Sentence Structure",
                     "R16: Sentence Beginnings"], index=[1])
        for i in range(len(text_characteristics[0])):
            new_data_row = [text_characteristics[0][i], text_characteristics[1][i], text_characteristics[2][i],
                                     text_characteristics[3][i], text_characteristics[4][i], text_characteristics[5][i],
                                     text_characteristics[6][i], easy_language_rules[0][i], easy_language_rules[1][i],
                                     easy_language_rules[2][i], easy_language_rules[3][i], easy_language_rules[4][i],
                                     easy_language_rules[5][i], easy_language_rules[6][i], easy_language_rules[7][i],
                                     easy_language_rules[8][i], easy_language_rules[9][i], easy_language_rules[10][i],
                                     easy_language_rules[11][i], easy_language_rules[12][i], easy_language_rules[13][i],
                                     easy_language_rules[14][i], easy_language_rules[15][i], easy_language_rules[16][i],
                                     easy_language_rules[17][i]]
            new_data_row_cleaned = [
                str(item) if isinstance(item, (list, tuple, dict)) else item for item in new_data_row
            ]
            df_sentence_level_results.loc[i] = new_data_row
        temp_df = df_sentence_level_results.iloc[:, [7, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]]
        number_of_all_rules = len(temp_df.columns)
        satisfied_rules = temp_df.sum(axis=1)
        df_sentence_level_results.insert(loc=7, column="Number of Satisfied Rules abs.", value=satisfied_rules)
        satisfied_rules_percentage = round((satisfied_rules / number_of_all_rules), 3)
        df_sentence_level_results.insert(loc=8, column="Amount of Satisfied Rules in %", value=satisfied_rules_percentage)
        return df_sentence_level_results

    def analyse_text_on_sentence_level(self, doc, title, nlp):
        all_text_characteristics = self.evaluate_text_characteristics(doc, title)
        all_rule_results = self.evaluate_Leichte_Sprache_rules(doc, nlp)
        df_sentence_level_results = self.create_sentence_level_df(all_text_characteristics, all_rule_results)
        return df_sentence_level_results