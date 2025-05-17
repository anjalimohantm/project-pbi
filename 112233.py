
import joblib

classi=joblib.load(r'C:\Users\ACER\\Titanic.pkl')
label1=joblib.load(r'C:\Users\ACER\lb.pkl')
label2=joblib.load(r'C:\Users\ACER\lb1.pkl')
stand=joblib.load(r'C:\Users\ACER\st.pkl')




import streamlit as st
st.title("Titanic survivor")
st.header("Data Analysis")

pclass=st. number_input("Enter your Pclass:")
Sex=st.selectbox("Select Sex:", ['female', 'male']) 
age=st. number_input("Enter your age:") 
sibsp=st.number_input("Enter your sibsp:") 
parch=st. number_input("Enter your Parch:") 
Fare=st. number_input("Enter your Fare:")
Embarked=st. selectbox("Select Embarked:", ['C', 'S'])

Sex=label1.transform([Sex])[0]
Embarked=label2.transform([Embarked])[0]

if st.button("predict"):
    result=classi.predict(stand.transform([[pclass,Sex,age,sibsp,parch,Fare,Embarked]]))[0]
    if result==0:
        st.success('Dead'.format(result))
    else:
        st.success('Alive'.format(result))
