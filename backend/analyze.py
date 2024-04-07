import re

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


EMOJIS = re.compile("["
                     u"\U0001F600-\U0001F64F"
                     u"\U0001F300-\U0001F5FF"
                     u"\U0001F680-\U0001F6FF"
                     u"\U0001F1E0-\U0001F1FF"
                     u"\U00002500-\U00002BEF"
                     u"\U00002702-\U000027B0"
                     u"\U00002702-\U000027B0"
                     u"\U000024C2-\U0001F251"
                     u"\U0001f926-\U0001f937"
                     u"\U00010000-\U0010ffff"
                     u"\u2640-\u2642" 
                     u"\u2600-\u2B55"
                     u"\u200d"
                     u"\u23cf"
                     u"\u23e9"
                     u"\u231a"
                     u"\ufe0f"
                     u"\u3030"
                     "]+", flags=re.UNICODE)

class Analyzer:
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def process(self, body):
        sentiment_scores = self.analyzer.polarity_scores(body)
        print(sentiment_scores)

    def clean(self, body):
        words = body.split()
        emojis_removed =  EMOJIS.sub(r'', words)
        urls_removed = [word for word in emojis_removed if not word.startswith('http://') and not word.startswith('https://')]
    
        return ' '.join(urls_removed)
    
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