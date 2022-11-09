import os
from Other.ResultAnalysis.BrokenRuleAnalyzer import BrokenRuleAnalyzer
from Other.ResultAnalysis.ReadabilityMetricsAnalyzer import ReadabilityMetricsAnalyzer
from Other.ResultAnalysis.SentimentAnalyzer import SentimentAnalyzer
import statistics as s


age1_text_level = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Evaluation/LS/Results/Text_Level_Results.xlsx"
age1_texts = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/age group 2 (selection preprocessed and shortened)/"

ls_corpus_texts = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Evaluation/LS/preprocessed/"

#broken_rule_analyzer = BrokenRuleAnalyzer(age1_text_level)
#print(broken_rule_analyzer.return_most_broken_rules_text_level())

readability_analyzer = ReadabilityMetricsAnalyzer(ls_corpus_texts)
wiener_sachtextformel = readability_analyzer.calculate_readability_score()
print(wiener_sachtextformel)

'''average_polarities_textblob = []
for file in os.listdir(age1_texts):
    if file.endswith(".txt"):
        with open(age1_texts + file, "r") as f:
            file_contents = f.read()
            sentiment_analyzer = SentimentAnalyzer(file_contents)
            text_polarity_textblob = sentiment_analyzer.analyze_sentiment_textblob()
            average_polarities_textblob.append(s.mean(text_polarity_textblob))

print(s.mean(average_polarities_textblob))'''
