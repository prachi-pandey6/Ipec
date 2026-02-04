import streamlit as st
st.title("age is")
age= st.number_input("enter your age",1,100)
city= st.selectbox("select your city", ["mumbai","delhi"])

if st.button("submit"):
  st.write("hello ", age, city)