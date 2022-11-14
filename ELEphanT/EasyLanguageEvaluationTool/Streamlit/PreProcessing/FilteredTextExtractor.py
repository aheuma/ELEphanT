import os
import pandas as pd
import shutil

def extract_file_indices(excel_file):
    tmp_file = pd.read_excel(excel_file)
    file_indices = tmp_file.loc[:, "No"]
    return file_indices

def copy_files(current_directory, target_directory, file_indices):
    for counter, textnr in enumerate(file_indices):
        if counter in file_indices:
            file = current_directory + str(textnr) + ".txt"
            shutil.copy(file, target_directory)
            print(file + " copied!")

input_path = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/ChildNov_entire corpus/"
output_path_age1 = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 1 (entire corpus)/"
output_path_age2 = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/age group 2 (entire corpus)/"

age_1_xlsx = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/text selection/age group 1 (6-8).xlsx"
age_2_xlsx = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/text selection/age group 2 (10-12).xlsx"

age_1_indices = extract_file_indices(age_1_xlsx)
age_2_indices = extract_file_indices(age_2_xlsx)

copy_files(input_path, output_path_age1, age_1_indices)
copy_files(input_path, output_path_age2, age_2_indices)