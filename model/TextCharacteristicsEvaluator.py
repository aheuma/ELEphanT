from decimal import Decimal


class TextEvaluator:

    def __init__(self):
        pass

    def remove_exponent(self, d):
        return d.quantize(Decimal(1)) if d == d.to_integral() else d.normalize()

    def evaluate_text_characteristics(self, doc, filename):
        filenames = []
        sentences = []
        sentence_numbers = []
        sentence_length_tokens = []
        sentence_length_words = []
        average_word_length = []
        sentence_length_characters = []
        for number, sent in enumerate(doc.sents):
            characters_per_sentence = 0
            words_per_sentence = 0
            filenames.append(filename)
            sentences.append(sent)
            sentence_numbers.append(number)
            sentence_length_tokens.append(len(sent))
            length_of_all_words = 0
            for token in sent:
                characters_per_sentence += len(token)
                if token.pos_ != "PUNCT":
                    words_per_sentence += 1
                    length_of_all_words += len(token)
            try:
                avg_word_length = round(length_of_all_words / words_per_sentence, 2)
                #avg_word_length = str(avg_word_length) This works but only by losing precision
                average_word_length.append(avg_word_length)
            except ZeroDivisionError:
                average_word_length.append(0)
            sentence_length_characters.append(characters_per_sentence)
            sentence_length_words.append(words_per_sentence)
        return filenames, sentences, sentence_numbers, sentence_length_tokens, sentence_length_words, average_word_length, sentence_length_characters

    def evaluate(self, doc, title):
        titles, sentences, sentence_numbers, sentence_length_tokens, sentence_length_words, average_word_length, sentence_length_characters = self.evaluate_text_characteristics(doc, title)
        return titles, sentences, sentence_numbers, sentence_length_tokens, sentence_length_words, average_word_length, sentence_length_characters