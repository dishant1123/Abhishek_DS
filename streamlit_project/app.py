import streamlit as st
import pandas as pd
import plotly.express as px

"""st.title("Student Registration App")

# sidebar

st.sidebar.header("student details")

name = st.sidebar.text_input("enter name?")
age =st.sidebar.number_input(
    "enter age",
    min_value=10,
    max_value=100
)   

course =st.sidebar.selectbox(
    "select course",
    ["python","data science","JAVA","MERN","Cyber Security"]
)

mode =st.sidebar.radio("select mode",["online","offline"])

experience =st.sidebar.slider(
    "select experience",
    min_value=1,
    max_value=10
)

# main page : 

st.header("Registration Form")

col1,col2 = st.columns(2)

with col1 :
    st.write("-------Student Details-------")
    st.write("name : ",name)
    st.write("age : ",age)
    st.write("course : ",course)
    
with col2 :
    st.write("-------Learning Details-------")
    st.write("mode : ",mode)
    st.write("experience : ",experience,"years")
    
# button

if st.button("Register"):
    if name :
        st.success(f'{name}  registered successfully')
    else :
        st.warning("please enter name")
"""
"""
st.title("Customer Data")

uploaded_file = st.file_uploader(
    "streamlit_project/customer_data (1).csv",
    type="csv",
)


if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    st.success("Data uploaded successfully")

    st.subheader("all customers data details")
    st.dataframe(df) 
    
    st.subheader("Dataset information")
    
    col1,col2 = st.columns(2)
    with col1 :
        st.metric("numbeer of  rows :",df.shape[0])
    with col2 :
        st.metric("numbeer of  columns :",df.shape[1])
        
    st.subheader("5 rows")
    st.dataframe(df.head()) 
    
    st.subheader("filter data")
    
    city = st.selectbox(
        "select city",
        df['City'].unique()
    )
    
    filter_df =df[df['City']==city]
    
    st.write("filter data : ")
    
    st.dataframe(filter_df)
    
else :
    st.info("please upload data/csv file")
"""

data =pd.DataFrame({
    'Month' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    "Sales" : [100,200,300,400,500,600,700,800,900,1000,1100,1200]
})


st.title("Monthly Sales")
fig = px.line(
    data,
    x="Month",
    y="Sales",
    title="Monthly Sales"
)

st.plotly_chart(fig,use_container_width=True)
