import os
import re
from statistics import mean
from pathlib import Path
import spacy
from spacy import Language
from spacy.matcher import DependencyMatcher, Matcher
import pandas as pd
from spacy import displacy
from collections import Counter

nlp = spacy.load("de_core_news_sm")


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


nlp.add_pipe("set_custom_boundaries", before="parser")

# sample_nominalisation_sent = "Das Gehen ist sehr anstrengend. Morgen beschäftige ich mich mit dem Laufen. Ich werde mir das Hören wieder beibringen."
# sample_sent_structure = "Zusammen fahren wir in den Urlaub. Wir gehen gemeinsam ins Kino. Solche Vögel heißen Strigiformes oder Caprimulgiformes."
# sample_passive_sents = "Der Hund wurde vom Mädchen gestreichelt. „Das Haus, in dem wir wohnen, ist gestrichen worden“, sagte sie. Das Essen wird zubereitet. Als ich entlassen wurde, hat es geregnet."
# sample_genitiv_sents = "Das Haus des Lehrers ist abgebrannt. Das ist der Mann der Stunde. Aufgrund des schlechten Wetters bleiben wir zuhause."
# sample_conjunctive_sents = "Morgen könnte es regnen. Ich würde das Haus kaufen. Wenn ich ein Auto hätte, müsste ich nicht laufen."
# sample_gender_sents = "Morgen gibt es Geld für Lehrerinnen und Lehrer. Die Autofahrer und Autofahrerinnen hupen. Verkäufer und Verkäuferinnen haben einen stressigen Job."
# sample_multiple_statement_sents = "Morgen gehen wir essen und du schläfst. Ich telefoniere gerade. Am Mittwoch wollen wir Fahrrad fahren, du gehst wandern, und Willi will schwimmen. Wenn ich morgen nach Hause komme, bist du arbeiten. Das Telefon klingelte, und ich nahm den Hörer ab."
# sample_foreign_material_sents = "Mein Job gefällt mir sehr gut. Das ist der Status Quo. Er ignorierte die subtilen Andeutungen."


path_to_txt_files = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Evaluation/LS/Dornröschen_LS.txt"

xlsx_file_agb_n = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Evaluation/Standard_vs_LS/Standardsprache/AGB_bpb_normal.xlsx"
xlsx_file_agb_ls = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Evaluation/Standard_vs_LS/LS/AGB_bpb_LS.xlsx"
xlsx_file = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Results/age group 1/49.xlsx"
xlsx_file2 = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Results/age group 2/62.xlsx"

p = Path(path_to_txt_files)
filename_with_extension = p.name
raw_filename = p.stem
print(filename_with_extension, raw_filename)
#filename_txt = re.sub("/.+/", "", filename)
#filename_number_only = filename_txt
#filename_number_only = filename_number_only.strip(".txt")

'''def calc_weighted_el_degree(xlsx_file):
    df = pd.read_excel(xlsx_file)
    if self.df["R1: High Numbers"].mean() < 1.00:
        rule1 = 0
    else:
        rule1 = 1
    if self.df["R2: Percentage Numbers"].mean() < 1.00:
        rule2 = 0
    else:
        rule2 = 1
    if self.df["R3: Written out Numbers"].mean() < 0.99:
        rule3 = 0
    else:
        rule3 = 1
    if self.df["R4: Special Characters"].mean() < 0.98:
        rule4 = 0
    else:
        rule4 = 1
    if self.df["R5: Repetitive Words"].mean() < 0.97:
        rule5 = 0
    else:
        rule5 = 1
    if self.df["R6: Sum: Long Words and Hyphens"].mean() < 0.65:
        rule6 = 0
    else:
        rule6 = 1
    if self.df["R7: Abbreviations"].mean() < 1.00:
        rule7 = 0
    else:
        rule7 = 1
    if self.df["R8: Nominalisations"].mean() < 0.88:
        rule8 = 0
    else:
        rule8 = 1
    if self.df["R9: Passive Voice"].mean() < 0.95:
        rule9 = 0
    else:
        rule9 = 1
    if self.df["R10: Genitive Case"].mean() < 0.94:
        rule10 = 0
    else:
        rule10 = 1
    if self.df["R11: Subjunctive Construct"].mean() < 1.00:
        rule11 = 0
    else:
        rule11 = 1
    if self.df["R12: Negative Words"].mean() < 0.92:
        rule12 = 0
    else:
        rule12 = 1
    if self.df["R13: Long Sentence"].mean() < 0.65:
        rule13 = 0
    else:
        rule13 = 1
    if self.df["R14: Multiple Sentence Statements"].mean() < 0.91:
        rule14 = 0
    else:
        rule14 = 1
    if self.df["R15: Complex Sentence Structure"].mean() < 0.33:
        rule15 = 0
    else:
        rule15 = 1
    if self.df["R16: Sentence Beginnings"].mean() > 0.08:
        rule16 = 1
    else:
        rule16 = 0
    all_rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16]
    sum_all_rules = sum(all_rules)
    return round(((sum_all_rules / len(all_rules)) * 100), 3)'''


# backreference with regex
# file_contents = re.sub("([a-z])\n([a-z])", "\\1 \\2", file_contents)
# file_contents = re.sub("([a-z])\n([A-Z])", "\\1 \\2", file_contents)
# file_contents = re.sub("([a-z]\,)\n([a-z])", "\\1 \\2", file_contents)
# file_contents = re.sub("([a-z]\,)\n([A-Z])", "\\1 \\2", file_contents)

# former approach on word duplicates
'''    def evaluate_word_repetitions(self, doc):
        word_repetitions_results = []
        unique_tokens = []
        number_of_all_tokens = 0
        unique_tokens_per_sent = 0
        for token in doc:
            if not token.is_stop and not token.is_punct:
                number_of_all_tokens += 1
                if token.text.lower() not in unique_tokens:
                    unique_tokens.append(token.text.lower())
        for number, sent in enumerate(doc.sents):
            for token in sent:
                if not token.is_stop and not token.is_punct:
                    if token.text.lower() in unique_tokens:
                        unique_tokens_per_sent += 1
            if unique_tokens_per_sent >= 1:
                word_repetitions_results.append(1)
            else:
                word_repetitions_results.append(0)
        return word_repetitions_results
'''

# with open(text_file, "r") as f:
'''file_contents = f.read()
    doc = nlp(file_contents)
    word_repetitions_results = []
    unique_tokens = []
    number_of_all_tokens = 0
    unique_tokens_per_sent = 0
    for token in doc:
        if not token.is_punct and token.pos_ == "NOUN":
            print(token, token.pos_)'''

# count different sentence start tokens
'''doc1 = list(doc.sents)
            sents_with_repetitive_sent_start = 0
            sent_start_words = []
            for number, sent in enumerate(doc.sents):
                for token in sent:
                    if token.i - sent.start == 0:
                        if token.pos_ == "PUNCT":
                            pass
                        elif token.pos_ != "PUNCT":
                            sent_start_words.append(token.text)
            for i in range(len(sent_start_words)-1):
                current_sent_start = sent_start_words[i]
                if sent_start_words[i] == sent_start_words[i+1]:
                    sents_with_repetitive_sent_start += 1
                if len(sent_start_words) - 1 == len(sent_start_words) - 2:
                    sents_with_repetitive_sent_start += 1'''

# Count number of commas in a sentence
'''comma_counter = 0
                                        for token in sent:
                                            if token.text == ",":
                                                comma_counter += 1
                                        if comma_counter >= 1:
                                            quantity_complex_sents += 1
                                    print(f"{quantity_complex_sents} Sätze von {len(doc1)} Sätzen folgen keinem einfachen Satzbau. Das sind {round(((quantity_complex_sents/len(doc1)) * 100), 3)}%!")
                        '''

# Determine chronolgy of subject and ROOT
'''            for number, sent in enumerate(doc.sents):
                                        counter = 0
                                        for token in sent:
                                            if token.dep_ == "sb":
                                                counter += 1
                                            elif token.dep_ == "ROOT":
                                                break
                                        if counter > 0:
                                            for token in sent:
                                                print(sent, token, token.dep_, spacy.explain(token.dep_))'''

# Access 1st Token in sent:
# if token.i - sent.start == 0

# former approach for nominalisations
'''  if token.text.istitle():
                                if token.pos_ == "VERB":
                                    token_dict = token.morph.to_dict()
                                    verbformInf = ("VerbForm", "Inf")
                                    if verbformInf in token_dict.items():
                                        print(token, "\t", sent)'''

# Testing different dep. matchers to find subjunctive clauses
'''
dep_pattern = [{"RIGHT_ID": "werden_verb", "RIGHT_ATTRS": {"LEMMA": "werden"}},
                       {"LEFT_ID": "werden_verb", "REL_OP": ">", "RIGHT_ID": "auxverb",
                        "RIGHT_ATTRS": {"TAG": {"IN": ["VVINF", "VMINF", "VAINF"]}}}]
#{""TAG": {IN": ["VVINF", "VMINF", "VAINF"]
#{"MORPH": "VerbForm=Inf"}'''

# Iterate over current sent and next sent
'''i = 0
            while i < (len(doc1)-1):
                if re.search("\?", str(doc1[i])) and re.search("[Nn]ein", str(doc1[i + 1])):
                    print(f"{str(doc1[i])} {str(doc1[i+1])}")
                i += 1'''

# lists with spacy tagsets
# pos_list = ["$(", "$", "$.", "ADJA", "ADJD", "ADV", "APPO", "APPR", "APPRART", "APZR", "ART", "CARD", "FM", "ITJ", "KOKOM", "KON", "KOUI", "KOUS", "NE", "NN", "NNE", "PDAT", "PDS", "PIAT", "PIS", "PPER", "PPOSAT", "PPOSS", "PRELAT", "PRELS", "PRF", "PROAV", "PTKA", "PTKANT", "PTKNEG", "PTKVZ", "PTKZU", "PWAT", "PWAV", "PWS", "TRUNC", "VAFIN", "VAIMP", "VAINF", "VAPP", "VMFIN", "VMINF", "VMPP", "VVFIN", "VVIMP", "VVINF", "VVIZU", "VVPP", "XY", "_SP"]
# dep_list = ["ROOT", "ac", "adc", "ag", "ams", "app", "avc", "cc", "cd", "cj", "cm", "cp", "cvc", "da", "dep", "dm", "ep", "ju", "mnr", "mo", "ng", "nk", "nmc", "oa", "oc", "og", "op", "par", "pd", "pg", "ph", "pm", "pnc", "punct", "rc", "re", "rs", "sb", "sbp", "svp", "uc", "vo"]

# Genitive prepositions
# genitive_prepositions = ["abzüglich", "zuzüglich", "angesichts", "anlässlich", "anstatt", "statt", "anstelle", "an Stelle", "aufgrund", "auf Grund", "außerhalb", "innerhalb", "oberhalb", "unterhalb", "dank", "entlang", "infolge", "inmitten", "kraft", "längs", "mangels", "mittels", "seitens", "vonseiten", "von Seiten", "trotz", "ungeachtet", "unweit", "während", "wegen", "zugunsten", "zu Gunsten", "zuungunsten", "zu Ungunsten", "zwecks"]
