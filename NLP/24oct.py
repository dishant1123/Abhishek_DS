# text classfication  models  : 
"""
1.  Naive Bayes
2.  logistic regression

Ex :  spam  , not spam 

1. congrats !!! you won  lottery  -----> spam 
2. hey , abhishek can we meet today ?? ----> not  spam 

how to  text classification  workflow 

1. collect labeled data
2. clean data
3. split 
4. convert text into  num features ----> bow, tf-idf
5. train model
6. predict
7. evaluate

alogrithms : 

1. Naive Bayes
2. logistic regression   ------> comopare -----> print accuracy
"""

import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

df = pd.read_csv("NLP/spam.csv",encoding='latin-1')

df =df[['v1','v2']]
df.columns = ['label','message']

print(df['label'].value_counts())

# feature selection :
X=df['message']
y=df['label']

# split data :
X_train, X_test, y_train, y_test = train_test_split(X,
                                                    y, 
                                                    test_size=0.2, 
                                                    random_state=42,
                                                    stratify=y)  # same proportion in both spam and ham 

# convert text into  num features ----> bow, tf-idf
tfidf_vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1,2),
    min_df=1,
    sublinear_tf=True,
)

X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# naive bayes :
nb_model = MultinomialNB(alpha=0.5)
nb_model.fit(X_train_tfidf, y_train)

# predict :
y_predict_nb = nb_model.predict(X_test_tfidf)

# accuracy :
print("accuracy nb : ",accuracy_score(y_test, y_predict_nb))
print("confusion matrix nb : ",confusion_matrix(y_test, y_predict_nb))
print("classification report nb : ",classification_report(y_test, y_predict_nb))

# logistic regression :
lr_model = LogisticRegression(class_weight='balanced',max_iter=1000)
lr_model.fit(X_train_tfidf, y_train)

# predict :
y_predict_lr = lr_model.predict(X_test_tfidf) 

# accuracy lr :
print("accuracy lr : ",accuracy_score(y_test, y_predict_lr))
print("confusion matrix lr : ",confusion_matrix(y_test, y_predict_lr))
print("classification report lr : ",classification_report(y_test, y_predict_lr))

# compare : 

results = pd.DataFrame({
    "model" :['Naive Bayes','Logistic Regression'],
    "accuracy" :[accuracy_score(y_test, y_predict_nb),
                 accuracy_score(y_test, y_predict_lr)]

})

print(results) 

# predict new msg : 

new_msg =[
    "hey abhishek can we meet today",

    "Congratulations you won a lottery",

    "Please send me a gift",

    "Wow you have won 1 crore rupees. Claim it now",

    "You are selected for a free cash prize. Call now",

    "URGENT! You have won 50000 rupees. Claim your prize now",

    "Free entry in a competition. Text WIN to 12345"
]

new_msg_tfidf = tfidf_vectorizer.transform(new_msg)

nb_predict = nb_model.predict(new_msg_tfidf)
lr_predict = lr_model.predict(new_msg_tfidf)

for i in range(len(new_msg)):
    print("new msg : ",new_msg[i])
    print("nb predict : ",nb_predict[i])
    print("lr predict : ",lr_predict[i])
    print("\n")
