import streamlit as st

st.write("""
Subtraction of 2 given numbers
""")
a=st.number_input("Enter the minuend")
b=st.number_input("Enter the subtrahend")
c=a-b
st.write(a, ' - ',b, ' = ',c)
