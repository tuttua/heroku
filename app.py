import streamlit as st

st.title('Subtraction of 2 given numbers')
minuend=st.number_input('Enter the minuend')
subtrahend=st.number_input('Enter the subtrahend')
difference=minuend-subtrahend
st.write(minuend, ' - ',subtrahend, ' = ',difference)
