import os
import spacy
from spacy.language import Language
import re

nlp = spacy.load("de_core_news_sm")

def count_quantity_of_sentences(path_to_directory):
    number_of_sentences_per_text = []
    for file in os.listdir(path_to_directory):
        if file.endswith(".txt"):
            with open(path_to_directory + file, "r") as f:
                file_contents = f.read()
                doc = nlp(file_contents)
                sentences = list(doc.sents)
                print(f"File: {file} \t number of sentences: {len(sentences)}")
                number_of_sentences_per_text.append(len(sentences))
    return number_of_sentences_per_text

def display_quantity_of_sentences(list_with_quantities_corpus1, list_with_quantities_corpus2):
    for i, j in zip(list_with_quantities_corpus1, list_with_quantities_corpus2):
        print(f"text corpus 1: {i} \t text corpus 2: {j} \t difference: {j-i}")

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

path_age1_preprocessed = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (selection preprocessed)/"
path_age2_preprocessed = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection preprocessed)/"
quantity_of_sentences_per_text_age1 = count_quantity_of_sentences(path_age1_preprocessed)
quantity_of_sentences_per_text_age2_pp = count_quantity_of_sentences(path_age2_preprocessed)

# compare quantity of sentences in age group 1 and 2
display_quantity_of_sentences(quantity_of_sentences_per_text_age1, quantity_of_sentences_per_text_age2_pp)

#Shorten texts of age group 2 according to the sentence lengths of age group 1.
#In the end, there are 14 sentence pairs with the same number of sentences.
#I.e.: The first texts from both corpora should both contain 757 sentences.
path_age2_preprocessed_shortened = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection preprocessed and shortened)/"
counter = 0

for file in os.listdir(path_age2_preprocessed):
    if file.endswith(".txt"):
        with open(path_age2_preprocessed + file, "r") as f:
            file_contents = f.read()
            doc = nlp(file_contents)
            for number, sent in enumerate(doc.sents):
                if number == quantity_of_sentences_per_text_age1[counter]-1:
                    sentence_end_char_position = sent.end_char
            #with open(path_age2_preprocessed_shortened + file, "w") as f2:
            #    f2.write(file_contents[:sentence_end_char_position])
            counter += 1

# compare quantity of sentences in both corpora again
quantity_of_sentences_per_text_age2_pp_s = count_quantity_of_sentences(path_age2_preprocessed_shortened)
display_quantity_of_sentences(quantity_of_sentences_per_text_age1, quantity_of_sentences_per_text_age2_pp_s)
