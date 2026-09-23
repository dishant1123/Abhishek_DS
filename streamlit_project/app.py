import streamlit as st

st.title("Student Registration App")

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
