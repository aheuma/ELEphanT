import os
import statistics


def count_length_of_files_in_folder(folder_path):
    lengths_of_files_in_folder = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(folder_path + file, "r") as f:
                file_contents = f.read()
                lengths_of_files_in_folder.append(len(file_contents))
    return lengths_of_files_in_folder


path_age1_entire_corpus = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (selection)/"
path_age2_entire_corpus = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (selection)/"

file_lengths_age1 = count_length_of_files_in_folder(path_age1_entire_corpus)
file_lengths_age2 = count_length_of_files_in_folder(path_age2_entire_corpus)

file_lengths_age1.sort(reverse=True)
print(f"Longest three texts of age group 1: {file_lengths_age1[0:3]}")
print(f"Median: {statistics.median(file_lengths_age1)}")
file_lengths_age2.sort()
print(file_lengths_age1, file_lengths_age2)
print(f"Shortest three texts of age group 2: {file_lengths_age2[0:3]}")
print(f"Median: {statistics.median(file_lengths_age2)}")