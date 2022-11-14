import os
import re

def find_and_print_uppercased_words(input_path):
    number_of_uppercased_words = 0
    for file in os.listdir(input_path):
        with open(input_path + file, "r") as f:
            file_contents = f.read()
            uppercased_words = re.findall("[A-Z]{2,}", file_contents)
            uppercased_words = list(dict.fromkeys(uppercased_words))
            number_of_uppercased_words += len(uppercased_words)
            for i in uppercased_words:
                print(i, file)
    print(f"Number of uppercased words in all text in a corpus: {number_of_uppercased_words}")

path_age1_selection = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (selection)/"
path_age2_selection = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection)/"

find_and_print_uppercased_words(path_age1_selection)
find_and_print_uppercased_words(path_age2_selection)