# text cleaning , processing and tokenization : 
"""
text processing  : process to  clean and  preaparing raw text data before feeding into the model

ex : 
'i love this product !!!!! it is  REALLY  useful and  helpful.' 

preprocessing :

love  this  product really useful helpful.


2. convert in to  lower 
3. remove  punctuation marks : ? , ; ! 

4. remove stop words : is am was were the a an and of in  

5. tokenize :
    a.words  : ex : i love pizza.  ----> ['i', 'love', 'pizza']
    b.sentences : ex : 
    [
     'i love pizza.i love pasta. i love pizza ,pasta and also burger.',
    ]
    output  :[
        'i love pizza',
        'i love pasta',
        'i love pizza,pasta and also burger.'
    ]
    c.subwords 
    d.individual characters

6.lemmatization : process to converting words into its  dictionary form

    ex : playing     play 
         played      play 
         studies     study
         running     run

"""

# ex : 1 remove punctuation marks

"""import  string 

s1 ='i love this product !!!!! it is  REALLY  useful and  helpful.' 

clean_text = s1.translate(str.maketrans('', '', string.punctuation))
print("original text : ",s1)
print("cleaned text : ",clean_text)
"""

# ex : 2 reomve the  stop words

"""import  nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

text = 'i love this product !!!!! it is  REALLY  useful and  helpful.'

stop_words = set(stopwords.words('english'))

words = text.lower().split()  #['i', 'love', 'this', 'product', 'it', 'is', 'really', 'useful', 'and', 'helpful']
clean_wrods = [] 

for i in words:
    if i not in stop_words:
        clean_wrods.append(i)

clean_text = ' '.join(clean_wrods)
print("original text : ",text)
print("cleaned text : ",clean_text)
"""

# ex : 3 tokenize

"""import nltk
nltk.download("punkt_tab")

text ='i love pizza. i love pasta. i love pizza burger.'

sentences = nltk.sent_tokenize(text)
words = nltk.word_tokenize(text)

print("sentences : ",sentences)
print("words : ",words)
"""

# ex : 4 lemmatization

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lemi = WordNetLemmatizer()

words = ['playing', 'played', 'studies', 'running']

for i in words:
    if i.endswith('ing') or i.endswith('ed'):   
        lemma = lemi.lemmatize(i, pos='v')
    elif i == 'studies':
        lemma = lemi.lemmatize(i, pos='v')
    else :
        lemma = lemi.lemmatize(i,pos='n')
    print(i,"->",lemma)
