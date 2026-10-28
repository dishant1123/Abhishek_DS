import pandas as pd 
import joblib 

model =joblib.load("churn_model.pkl")

# new  customer data  : 

new_customer =pd.DataFrame({
    'tenure' :[4],
    'monthly_charges' :[900],
    'supportcalls' :[5]
})

prediction  =model.predict(new_customer)

print(new_customer)
print(prediction[0])