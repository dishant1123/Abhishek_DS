import  pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import  RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report 
import joblib 


data ={
    'tenure' :[
        2,5,8,12,24,36,
        6,30,18,3,28,10
    ],
    'monthly_charges' :
    [
      950,850,700,600,550,500,
      450,400,350 ,200,250,220 
    ],
    
    'supportcalls':[
        5,4,3,2,1,0,
        4,1,2,6,1,3
    ],
    'chrun' :[
        'yes','yes','yes','yes','no',
        'no','no','no','yes','no', 
        'yes','no' 
    ]
    
    
}

df = pd.DataFrame(data)
print(df)

X=df[['tenure','monthly_charges','supportcalls']]
y=df['chrun']

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# model 

model =RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("accuracy score : ",accuracy_score(y_pred,y_test))
print("classification report : ",classification_report(y_pred,y_test))

# save  model : 

joblib.dump(model,'churn_model.pkl')

print("model save  successfully ")

