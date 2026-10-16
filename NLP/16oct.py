# NLP  :
"""
branch of  AI  ------> help   ----> computer  enable to understand the analysis of the data  ----> generate human languages  

Real life examples :
1. chatbots
2. google assistant
3. chartgpt 

lib  : nltk 

"""

# ex :1 

import nltk
from nltk.tokenize import word_tokenize

"""nltk.download('punkt_tab')  
text = "I am a python programmer"

words = word_tokenize(text)  # splits the text into individual words
print("original text : ",text)
print("tokenized text : ",words)
print("number of words : ",len(words))
"""

# why use  AI ? 
"""
1. automation  : 
2. time saving
3. language translation
4. decision making : identifying the  pattern of text data 
5. customer service / support
"""

# ex :2 
from  collections import Counter
import  re
"""
feedback =[
    "The  product is excellent",
    "the product is good",
    "the product is very good",
    "the product is poor",
    "the product is excellent"
]

words =[] 

for i in  feedback:
    word =re.findall(r'\b[a-z]+\b',i)
    words.extend(word)

word_count =Counter(words)
print(word_count)
"""

# sentiment analysis : 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

"""
s = SentimentIntensityAnalyzer()

reviews = [
    "This product is amazing.",
    "I hate this product.",
    "The product arrived today.",
    "The service was terrible.",
    "The delivery was fast.",
]

for  i in  reviews:
    score = s.polarity_scores(i)
    
    if score['compound'] > 0.05:
        sentiment = 'positive'
    elif score['compound'] < -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    print("Review:", i)
    print("Sentiment:", sentiment)
    print("score:", score['compound'])
"""  
"""
score > 0.05 ----> positive
score < -0.05 ----> negative
score = 0 ------> neutral

""" 

# language translation :

"""from transformers import pipeline

translator = pipeline('translation', 
                      model='Helsinki-NLP/opus-mt-en-fr')

text = "hello , how are you ?"

result = translator(text)
print("english : ",text)
print("german : ",result[0]['translation_text'])

"""

