# The files 197.txt (corpus 2) and 485.txt (corpus 1) are of the same length, as well as the files 178.txt (corpus 2) and 301.txt (corpus 1)

library("quanteda")
library("quanteda.textstats")
library("readtext")
texts <- readtext("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Readability Test/*.txt", cache = FALSE)
text_corpus <- corpus(texts)
summary(text_corpus)
readability <- textstat_readability(text_corpus, c("meanSentenceLength", "meanWordSyllables", "Flesch.Kincaid", "Flesch"), remove_hyphens = TRUE, min_sentence_length = 1, max_sentence_length = 10000, intermediate = FALSE)
head(readability)

corpus_directory = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Readability Test/"
file1 <- "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Readability Test/178.txt"
file2 <- "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Readability Test/197.txt"
file3 <- "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Readability Test/301.txt"
file4 <- "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/quantils/Textfiles/Readability Test/485.txt"

file1_tokenized <- tokenize(file1, lang="en")
file2_tokenized <- tokenize(file2, lang="en")
file3_tokenized <- tokenize(file3, lang="en")
file4_tokenized <- tokenize(file4, lang="en")

file1_flesch <- flesch(file1_tokenized)
file1_fk <- flesch.kincaid(file1_tokenized)
print(file1)
print(file1_flesch)
print(file1_fk)

file2_flesch <- flesch(file2_tokenized)
file2_fk <- flesch.kincaid(file2_tokenized)
print(file2)
print(file2_flesch)
print(file2_fk)

file3_flesch <- flesch(file3_tokenized)
file3_fk <- flesch.kincaid(file3_tokenized)
print(file3)
print(file3_flesch)
print(file3_fk)

file4_flesch <- flesch(file4_tokenized)
file4_fk <- flesch.kincaid(file4_tokenized)
print(file4)
print(file4_flesch)
print(file4_fk)