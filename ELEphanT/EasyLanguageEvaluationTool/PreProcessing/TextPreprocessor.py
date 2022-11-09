import os
import re


class TextPreprocessor:

    def __init__(self, original_txt_input, preprocessed_txt_output):
        self.original_txt_input = original_txt_input
        self.preprocessed_txt_output = preprocessed_txt_output

    def preprocess_texts(self):
        for file in os.listdir(self.original_txt_input):
            if file.endswith(".txt"):
                with open(self.original_txt_input / file, "r") as f:
                    print("Preprocessing file: " + file)
                    file_contents = f.read()

                    # Normalisation of french quotation marks because the german ones are better recognized.
                    # Apostrophes are also replaced by the german character because of consistency.
                    file_contents = re.sub("»", "„", file_contents)
                    file_contents = re.sub("«", "“", file_contents)
                    file_contents = re.sub("›", "‚", file_contents)
                    file_contents = re.sub("‹", "‘", file_contents)
                    file_contents = re.sub("\'", "’", file_contents)

                    # Normalization of different variants of false whitespaces and paragraphs.
                    file_contents = re.sub("\s{2,}", " ", file_contents)
                    file_contents = re.sub("\. “", ".“", file_contents)
                    file_contents = re.sub("– “", "–“", file_contents)
                    file_contents = re.sub("\n+", " ", file_contents)
                    file_contents = re.sub("\s{2,}\n", " ", file_contents)
                    file_contents = re.sub("\t", " ", file_contents)
                    file_contents = re.sub("^ ", "", file_contents)

                    # Normalization of text-specific aspects.
                    file_contents = re.sub("∙", "-", file_contents)
                    file_contents = re.sub("·", "-", file_contents)
                    file_contents = re.sub("\$SB\$", "", file_contents)
                    file_contents = re.sub("Mrs. ", "Mrs ", file_contents)
                    file_contents = re.sub("Mr. ", "Mr ", file_contents)
                    file_contents = re.sub("\?\?\?", "Fragezeichen", file_contents)
                    file_contents = re.sub("\!\!\!", "Ausrufezeichen", file_contents)

                    # Create new filename for preprocessed file
                    filename = self.original_txt_input / file
                    filename_without_extension = filename.stem
                    new_filename = filename_without_extension + "_preprocessed.txt"

                    with open(self.preprocessed_txt_output / new_filename, "w") as f2:
                        f2.write(file_contents)
