# deep learning  in  NLP  : 
"""
computer  also  understand  the  human  languages . 

ex : sentiment  analysis , chart bots  etc 

limitation  : 
1.limited context understanding 
2.limited understanding of  word relationship 
3.very  difficult  to  understand the complex languages   

transformers : 
model  : 

1.BERT : to understand the context from both  directions in sentence. ---> classification 
2.GPT:    used for  chart bots 
3.DistilBERT : small ,faster 

attention machanism  : word importance  in  sentense.  

huuging face : open source platform ,pretrained model  ---> which used in NLP ,LLM 

"""

# movie  imdb rating  data set sentiment analysis : 

import  pandas as pd 
from  datasets import load_dataset 

from transformers import pipeline
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix 

dataset =load_dataset("stanfordnlp/imdb",
                      split="train[:20]")

df =pd.DataFrame(dataset)

print(df.head())

classifer = pipeline("sentiment-analysis",
                    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")



review = "the movie was excellent and  the action was fantastic."

result = classifer(review)
print("review : ",review)
print("predict senti : ",result[0]['label'])

print("confidence score : ",round(result[0]['score'],2))

test_dataset =load_dataset("stanfordnlp/imdb",
                      split="test")
df_test =pd.DataFrame(test_dataset)

y_actual =df_test['label'].tolist() 

test_review = df_test['text'].tolist() 

# predict senti : 

test_preidct = classifer(test_review ,truncation=True) 

y_predict =[] 

for i in test_preidct:
    y_predict.append(i['label'])

# accuracy : 
accuracy = accuracy_score(y_actual,y_predict) 
print("accuracy score is : ",accuracy) 