import io
import string

import emoji
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class Analyzer:
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.companies = self.__init_companies('data/cleaned_nasdaq.csv')
        print(self.companies)

    def process(self, body):
        sentiment_scores = self.analyzer.polarity_scores(body)
        return sentiment_scores['compound']

    def clean(self, body):
        emojis_removed = emoji.replace_emoji(body, replace='')
        urls_removed = [word for word in emojis_removed.split() if not word.startswith('http://') and not word.startswith('https://')]
        punctuation_removed = [char for char in ' '.join(urls_removed) if char not in string.punctuation]
        
        return ''.join(punctuation_removed)
    
    def get_companies(self, body):
        entities = self.__get_entities(body)
        res = set()
        for entity in entities:
            if entity in self.companies:
                res.add(self.companies[entity])
            else:
                entity_words = entity.split(" ")
                for word in entity_words:
                    if word in self.companies:
                        res.add(self.companies[word])
        return res
    
    def __init_companies(self, fileName):
        res = {}
        prev = ''
        with open(fileName, 'r') as inStream:
            for row in inStream:
                cur = row.strip().split(',')
                if cur[1] == prev:
                    continue
                res[cur[1]] = cur[0]
        return res

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
                    res.add(named_entity)
                    cur = []
            else:
                continue
        
        return res