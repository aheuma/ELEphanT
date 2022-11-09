import os
import re
import random
import shutil

'''Copy texts of age group 1 corpus with length >=20000 and <= 50000
This selection is due to the distribution of character quantities per text file in corpus 1.
The most files (14) contained between 20000 and 50000 characters so it was decided to choose these 14 files.
One reason is that texts need to be long enough for the final analysis; 
at the same time, the distribution of file length should not differ too much'''

path_age1_entire_corpus = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (entire corpus)/"
path_age1_selection = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (selection)/"

for file in os.listdir(path_age1_entire_corpus):
    if file.endswith(".txt"):
        with open(path_age1_entire_corpus + file, "r") as f:
            file_to_copy = path_age1_entire_corpus + file
            file_contents = f.read()
            if(len(file_contents) >= 20000 and len(file_contents) <= 50000):
                shutil.copy(file_to_copy, path_age1_selection)
                print(file, "; Länge:", len(file_contents), "Zeichen")

# Selection of 14 random texts of age group 2 corpus
# For further processing of texts, the texts are shortened to under 100000 characters.
path_age2_entire_corpus = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (entire corpus)/"
path_age2_selection = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection)/"

all_files_age2 = os.listdir(path_age2_entire_corpus)
chosen_files_age2 = random.sample(all_files_age2, k=14)
copied_texts = []

for file in os.listdir(path_age2_entire_corpus):
    if file.endswith(".txt"):
        if file in chosen_files_age2:
            file_to_copy = path_age2_entire_corpus + file
            with open(file_to_copy, "r") as f:
                file_contents = f.read()
                with open(path_age2_selection + file, "w") as f2:
                    f2.write(file_contents[0:99999])
            copied_texts.append(file_to_copy)

print("Anzahl Zufallstexte:", len(chosen_files_age2))
print("Anzahl kopierter Texte:", len(copied_texts))