import re
import spacy
from spacy.lang.de import German
from spacy.pipeline import sentencizer
from spacy.language import Language
from textblob_de import TextBlobDE
import stanza

test_file = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection shortened)/190.txt"
#file_out = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Textfiles/Altersgruppe 2 (Auswahl bereinigt)/190.txt"

# Modifying spaCy sentence boundaries
# Currently: program enables to modify sentence boundaries for custom needs

#nlp = German()
#nlp.add_pipe("sentencizer")
nlp = spacy.load("de_core_news_sm")
#sentence_end_chars = [".", "…","!", "?", "??", "???", "!!", "!!!", "?!", "!?", ".«", ".“"]
#segmentator = sentencizer.make_sentencizer(nlp=German(), name="sentencizer", punct_chars = sentence_end_chars, overwrite=False, scorer="spacy.senter_scorer.v1")
#nlp.add_pipe("sentencizer")
@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == "…":
            doc[token.i + 1].is_sent_start = True
        elif token.text == ";":
            doc[token.i + 1].is_sent_start = False
    return doc
nlp.add_pipe("set_custom_boundaries", before="parser")
with open(test_file, "r") as f:
    file_contents = f.read()
    doc = nlp(file_contents)
    for i, sentence in enumerate(doc.sents):
        print(i, sentence)

# Testing stanza's sentence segmentation
nlp = stanza.Pipeline(lang="de", processors="tokenize")

with open(test_file, "r") as f:
    file_contents = f.read()
    doc = nlp(file_contents)
    for i, sentence in enumerate(doc.sentences):
        print(i, sentence.text)

# Testing TextBlob's sentence segmentation
with open(test_file, "r") as f:
    file_contents = f.read()
    blob = TextBlobDE(file_contents)
    for number, sentence in enumerate(blob.sentences):
        print(number, sentence)