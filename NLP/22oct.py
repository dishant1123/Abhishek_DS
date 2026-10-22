import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

df =pd.read_csv("NLP/Womens Clothing E-Commerce Reviews.csv")

# col selection
df = df[['Review Text','Rating']].copy()
# print(df.info())
# print(df.isnull().sum())

#remove rows with missing values :

df =df.dropna(subset=['Review Text']).copy()
df['Review Text'] = df['Review Text'].str.lower()
df =df.drop_duplicates(subset=['Review Text']).copy()

# 100 senetences : 

sample_df = df.head(100).copy()
documents  =sample_df['Review Text'].values.tolist()

# print("documents : ",len(documents)) 
# print("documents : ",documents[0])

# BOW : 
bow_vectorizer = CountVectorizer(
    stop_words='english',
    max_features=100
)
bow_matrix=bow_vectorizer.fit_transform(documents)
bow_vocal = bow_vectorizer.get_feature_names_out()

# print("bow matrix : ",bow_matrix.shape)
# print("bag of words vocal : ",bow_vocal)

# dataframe : 
bow_df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=bow_vocal,
    index=sample_df.index
)
# print("bow dataframe : ",bow_df.head())

# find word frequency :

word_freq = bow_df.sum(axis=0)
word_freq = word_freq.sort_values(ascending=False)

# print("word frequency :\n ",word_freq.head(10))

"""top_words = word_freq.head(10)
plt.figure(figsize=(10,5))

top_words.sort_values().plot(kind='barh',color='blue',title='Top 10 words in reviews')
plt.xlabel('Frequency')
plt.ylabel('Words')
plt.tight_layout()
plt.show()
"""
#  TF-IDF vectorizer :

tfidf_vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=100
)
tfidf_matrix=tfidf_vectorizer.fit_transform(documents)
tfidf_vocal = tfidf_vectorizer.get_feature_names_out()

# convert dataframe :

tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=tfidf_vocal,
    index=sample_df.index
)

# compare bow and tfidf :

print("bow matrix : ",bow_matrix.shape)
print("tfidf matrix : ",tfidf_matrix.shape)

# save : 

bow_df.to_csv("cutomer_reviews_bow.csv")
tfidf_df.to_csv("cutomer_reviews_tfidf.csv")

word_freq.to_csv("word_frequency.csv",header=['frequency'])

print("\n file saves successfully !!!!")
print("1. cutomer_reviews_bow.csv")
print("2. cutomer_reviews_tfidf.csv")
print("3. word_frequency.csv")