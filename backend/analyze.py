import re
import string

import emoji
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class Analyzer:
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def process(self, body):
        sentiment_scores = self.analyzer.polarity_scores(body)
        print(sentiment_scores)

    def clean(self, body):
        emojis_removed = emoji.replace_emoji(body, replace='')
        urls_removed = [word for word in emojis_removed.split() if not word.startswith('http://') and not word.startswith('https://')]
        punctuation_removed = [char for char in ' '.join(urls_removed) if char not in string.punctuation]
        
        return ''.join(punctuation_removed)
    
    def get_companies(self, body):
        entities = self.__get_entities(body)
        for entity in entities:
            pass
        return entities
    
    def __get_entities(self, body):
        bodyTokenized = nltk.word_tokenize(body)
        bodyTagged = nltk.pos_tag(bodyTokenized)
        bodyChunked = nltk.ne_chunk(bodyTagged)
        
        res = set()
        cur = []
        
        for chunk in bodyChunked:
            if type(chunk) == nltk.tree.Tree:
                cur.append(" ".join([token for token, _ in chunk.leaves()]))
            if cur:
                named_entity = " ".join(cur)
                if named_entity not in res:
                    res.add(cur)
                    cur = []
            else:
                continue
        
        return res