# ELEphanT – Easy Language Evaluation Tool


<img src="https://user-images.githubusercontent.com/92684499/200805059-bbe7f67e-63c8-4674-908c-fea0786d3ce9.png" align="left" width="230"/>

## Description
This student project is embedded in the DFG-funded project "CHYLSA – Advanced sentiment analysis for understanding affective-aesthetic responses to literary texts: A computational and experimental psychology approach to children’s literature" at Johannes Gutenberg-Universität (JGU) Mainz and Freie Universität Berlin and is part of the master program "Digitale Methodik in den Geistes- und Kulturwissenschaften" (Digital Humanities) at the JGU. <br> It aims at analyzing a given text in terms of its compliance to a specific ruleset of Easy Language. This includes recherche regarding Easy Language theory, rulebooks and automatic text simplification. The chosen rulebook is then implemented in Python to develop a tool that measures the degree of Easy Language and returns an Easy Language score.

<br clear="left"/>

## Easy Language
Easy Language is a German language variety distinguished by simplicity, a clear text formating and firm rules. In Germany, the influence of Leichte Sprache increased strongly in the first decade of 2000 when the Federal Act on Equality for People with Disabilities (in 2002) and its realization, the "Barrierefreie-Informationstechnik-Verordnung" (BITV 2.0) (Accessible Information Technology Regulation) in 2011, were adopted. <br>
In a broader sense, Easy Language targets all people that can't deal properly with a standard text and would prefer a more simple version. Concretely, this includes groups such as functional illiterate people, people suffering from Dementia, hearing impaired people, foreign language learners etc. <br>
There is no standard rulebook for Easy Language. Instead, there are multiple rulebooks, in most cases with either a strongly scientific oder practical-political background. For this project, the rulebook by [Netzwerk Leichte Sprache](https://www.leichte-sprache.org/wp-content/uploads/2017/11/Regeln_Leichte_Sprache.pdf) has been chosen, due to its popularity, among other things. 

## Preliminary Remarks
- ELEphanT analyzes either a single text or multiple texts.
- In the runtime, the original files will be modified / pre-processed; the modified files will be safed at a specified location.
- There will be a two-fold output: <br>
    a. For each analyzed text file, there will be an excel file containing the tool's results. <br>
    b. There will be one additional summarizing excel file – this is interesting in cases where you would like to compare different texts in terms of Easy Language.

## Installation   
1. Clone repository.
2. Open file: \ELEphanT\EasyLanguageEvaluationTool\ELEphanT.py.
3. Specify the necessary paths in ELEphanT.py: <br>
    a. Path to your original txt-files to be analyzed. (Please note: All txt-files in this folder will be analyzed.) <br>
    b. Path to location for preprocessed txt-files. <br>
    c. Path to location for sentence level results (a file with results (one line = one sentence) for each original txt-file will be generated). <br>
    d. The filename for another excel file with summarizing text level results (optional).
4. Install the following necessary packages via pip or anaconda: <br>
    a. [spaCy](https://spacy.io/usage) <br>
    b. [pandas](https://pandas.pydata.org/docs/getting_started/install.html) <br>
    c. [xlsxwriter](https://pypi.org/project/XlsxWriter/) <br>
    d. [openpyxl](https://pypi.org/project/openpyxl/)
5. Download spaCy's German language model [de_core_news_sm](https://spacy.io/models/de#de_core_news_sm) with the terminal command "python3 -m spacy download de_core_news_sm" 
6. In your terminal, locate to ...\ELEphanT\EasyLanguageEvaluationTool\ and run ELEphanT.py.

**Remarks**
- Required input text format: .txt
- Python version: Python 3.10

## References
The logo has been developed on the basis of free resources from vecteezy.com. <br>
Artist: Vecteezy <br>
Vector graphic: [Elephan Vectors](https://www.vecteezy.com/vector-art/2485692-elephant-kids-coloring-page-great-for-beginner-coloring-book) 
