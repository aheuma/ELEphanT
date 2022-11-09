library(openxlsx)
library(syuzhet)
library(stringr)

# corpus_directory = Pfad zu den bereinigten txt-Dateien 
corpus_directory = "/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/age group 1 (selection preprocessed)"

corpus_files <- list.files(corpus_directory, pattern="txt", full.names=TRUE)
poemCorpus <- sapply(corpus_files, read.delim, header=FALSE, sep="\n", fill=TRUE, USE.NAMES = TRUE)
poemCorpus <- unname(poemCorpus)

# files_without_path: erzeugt eine Liste, die die Namen der Dateien ohne Dateipfad und -endung enthält
# files_without_path werden benutzt, um Spalte 1 in der Ergebnistabelle zu füllen (die Titel der Gedichte)
# Zeile 15: Die doppelten back-slahes escapen den normalen Slash; wichtig: am Ende des regex steht \\//
files_without_path <- str_remove(corpus_files, "\\/home\\/anneleheu\\/Documents\\/Masterstudium\\/M8\\/Praxisprojekt\\/Other: Code\\/Textfiles\\/age group 1 (selection preprocessed)\\//")
files_without_path <- str_remove(files_without_path, ".txt")

# Schleife, die die einzelnen Excel-Dateien mit Sentiment-Daten erstellt
for(i in 1:length(poemCorpus)){
  workbook = createWorkbook()
  addWorksheet(workbook, "Sentiment Results")
  
  # Berechnung von Sentiments und Emotions für jedes Gedicht
  sentiment_emotion_values <- get_nrc_sentiment(poemCorpus[[i]], language = "german", lowercase =	FALSE)
  
  # Berechnung des unären Valence-Scores für jedes Gedicht
  unary_valence_score <- (sentiment_emotion_values[,9]*-1) + sentiment_emotion_values[,10]
  
  valence_score_with_header <- c("valence", unary_valence_score)
  
  # Erzeugung zweier Vektoren:
  # 1. Trägt den Titel des jeweiligen Gedichts in jeder Zeile und ist so lang wie das Gedicht.
  # 2. Enthält Zahlen für die Zeilennummerierung.
  poem_title_column <- rep(files_without_path[[i]], length(poemCorpus[[i]]))
  poem_lines <- 1:length(poemCorpus[[i]])
  
  # Ergebnisse werden in die Excel-Datei geschrieben als .xlsx gespeichert
  writeData(workbook, sheet = "Sentiment Results", c("poem title", poem_title_column), startRow = 1, startCol = 1)
  writeData(workbook, sheet = "Sentiment Results", c("poem line", poem_lines), startRow = 1, startCol = 2)
  writeData(workbook, sheet = "Sentiment Results", c("poem content", poemCorpus[[i]]), startRow = 1, startCol = 3)
  writeData(workbook, sheet = "Sentiment Results", sentiment_emotion_values, startRow = 1, startCol = 4)
  writeData(workbook, sheet = "Sentiment Results", valence_score_with_header, startRow = 1, startCol = 14)
  saveWorkbook(workbook, file=paste0("/home/anneleheu/Documents/Masterstudium/M8/Praxisprojekt/Other: Code/Textfiles/Results/Sentiment Analysis (R)/age group 1/", files_without_path[[i]], ".xlsx", sep=""), overwrite = TRUE)
}
