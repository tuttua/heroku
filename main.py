import streamlit as st

st.title('Subtraction of two numbers')
num1 = st.number_input("Enter the minuend")
num2 = st.number_input("Enter the subtrahend")
c=num1-num2
st.write(num1, ' - ',num2, ' = ',c)
