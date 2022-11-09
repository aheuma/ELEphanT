import os
import pandas as pd


class StatisticsAnalyzer:
    def __init__(self):
        pass

    def print_mean_median_std_modus(self, directory_sentence_level_results):
        for file in os.listdir(directory_sentence_level_results):
            if file.endswith(".xlsx"):
                df = pd.read_excel(directory_sentence_level_results + file)
                tmp_df = df.iloc[:, 6]
                average_satisfied_rules = tmp_df.mean()
                median_satisfied_rules = tmp_df.median()
                std_satisfied_rules = tmp_df.std()
                modus_satisfied_rules = tmp_df.value_counts()
                print(
                    f"Mean: {average_satisfied_rules} \t Median: {median_satisfied_rules} \t St. Dev.: {std_satisfied_rules} \t Modus: {modus_satisfied_rules}")