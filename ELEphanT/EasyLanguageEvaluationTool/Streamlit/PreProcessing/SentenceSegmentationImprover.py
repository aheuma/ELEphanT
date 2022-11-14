import os
import spacy
import re

nlp = spacy.load("de_core_news_sm")

# find chapter annotations "$SB$"
def find_chapter_markers(input_path):
    for file in os.listdir(input_path):
        if file.endswith(".txt"):
            with open(input_path + file, "r") as f:
                file_contents = f.read()
                file_contents = re.sub("\s{2,}", " ", file_contents)
                file_contents = re.sub("^ ", "", file_contents)
                file_contents = re.sub("\. “", ".“", file_contents)
                # file_contents = re.sub("\n+", " ", file_contents)
                file_contents = re.sub("\s{2,}\n", " ", file_contents)
                matches = re.findall("\$SB\$", file_contents)
                for i in matches:
                    print(i, file)


def find_chapter_titles(input_path):
    for file in os.listdir(input_path):
        if file.endswith(".txt"):
            with open(input_path + file, "r") as f:
                file_contents = f.read()
                print(file, re.findall("\t", file_contents))
                # file_contents = re.sub("\s{2,}", " ", file_contents)
                # file_contents = re.sub("^ ", "", file_contents)
                # file_contents = re.sub("\. “", ".“", file_contents)
                # file_contents = re.sub("\n+", " ", file_contents)
                # file_contents = re.sub("\s{2,}\n", " ", file_contents)
                # file_contents = re.sub("([a-z])\n([a-z])", "\\1 \\2", file_contents)
                # file_contents = re.sub("([a-z])\n([A-Z])", "\\1 \\2", file_contents)
                # file_contents = re.sub("([a-z]\,)\n([a-z])", "\\1 \\2", file_contents)
                # file_contents = re.sub("([a-z]\,)\n([A-Z])", "\\1 \\2", file_contents)
                # file_contents = re.sub("»", "„", file_contents)
                # file_contents = re.sub("«", "“", file_contents)
                # file_contents = re.sub("›", "‚", file_contents)
                # file_contents = re.sub("‹", "‘", file_contents)

                # doc = nlp(file_contents)
                # for number, sent in enumerate(doc.sents):
                #    for token in sent:
                #        print(number, token, token.pos_)

                # print(file_contents)

# age group 1
path_age1_selection = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (selection 2)/"
path_age1_preprocessed = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (selection preprocessed)/"
#find_chapter_markers(path_age1_selection)
find_chapter_titles(path_age1_preprocessed)

# age group 2
path_age2_selection = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection 2)/"
path_age2_preprocessed = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection preprocessed)/"
#find_chapter_markers(path_age2_selection)
find_chapter_titles(path_age2_preprocessed)
