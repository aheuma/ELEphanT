import os
import re


class TextPreprocessor:

    def __init__(self):
        pass

    def preprocess_texts(self, text):
        preprocessed_text = text

        # Normalisation of french quotation marks because the german ones are better recognized.
        # Apostrophes are also replaced by the german character because of consistency.
        preprocessed_text = re.sub("»", "„", preprocessed_text)
        preprocessed_text = re.sub("«", "“", preprocessed_text)
        preprocessed_text = re.sub("›", "‚", preprocessed_text)
        preprocessed_text = re.sub("‹", "‘", preprocessed_text)
        preprocessed_text = re.sub("\'", "’", preprocessed_text)

        # Normalization of different variants of false whitespaces and paragraphs.
        preprocessed_text = re.sub("\s{2,}", " ", preprocessed_text)
        preprocessed_text = re.sub("\. “", ".“", preprocessed_text)
        preprocessed_text = re.sub("– “", "–“", preprocessed_text)
        preprocessed_text = re.sub("\n+", " ", preprocessed_text)
        preprocessed_text = re.sub("\s{2,}\n", " ", preprocessed_text)
        preprocessed_text = re.sub("\t", " ", preprocessed_text)
        preprocessed_text = re.sub("^ ", "", preprocessed_text)

        # Normalization of text-specific aspects.
        preprocessed_text = re.sub("∙", "-", preprocessed_text)
        preprocessed_text = re.sub("·", "-", preprocessed_text)
        preprocessed_text = re.sub("\$SB\$", "", preprocessed_text)
        preprocessed_text = re.sub("Mrs. ", "Mrs ", preprocessed_text)
        preprocessed_text = re.sub("Mr. ", "Mr ", preprocessed_text)
        preprocessed_text = re.sub("\?\?\?", "Fragezeichen", preprocessed_text)
        preprocessed_text = re.sub("\!\!\!", "Ausrufezeichen", preprocessed_text)

        return preprocessed_text
