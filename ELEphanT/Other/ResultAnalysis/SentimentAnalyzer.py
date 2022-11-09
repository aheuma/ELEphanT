from textblob_de import TextBlobDE as TextBlob


class SentimentAnalyzer:

    def __init__(self, text):
        self.text = text
        self.blob = TextBlob(self.text)

    def analyze_sentiment_textblob(self):
        text_polarity = []
        for sentence in self.blob.sentences:
            text_polarity.append(sentence.sentiment.polarity)
        return text_polarity

