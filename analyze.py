import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


class Analyzer:
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def process(self, body):
        sentiment_scores = self.analyzer.polarity_scores(body)
        print(sentiment_scores)

    def clean(self, data):
        return data