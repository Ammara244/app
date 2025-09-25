import streamlit as py

st.header('slider widget')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.header('creating a key:')
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.header('checkbox:')
if st.checkbox('Show '):
  st.write('boo')


st.header('selectbox:')
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
