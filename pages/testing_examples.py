import streamlit as py

st.subheader('slider widget')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.subheader('creating a key:')
import streamlit as st
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

st.subheader('checkbox:')
if st.checkbox('Show '):
  st.write('boo')


st.subheader('selectbox:')
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option
