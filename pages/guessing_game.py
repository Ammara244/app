import streamlit as st
import random

name = st.text_input('Enter your name:')
if name:
    st.write('Hello, ', name, '!')

st.write("Pick a page from the sidebar to start:")

st.title('🎲 Number Guessing Game')
st.write(name, 'try to guess what my number is between 1 and 100')

# stores a number that wont reset every time
#creates it for the first time then it doesnt change after
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
# user picks number using a slider
guess = st.slider('Pick a number', 1, 100, 50)
# make a button:
if st.button('Check my answer'):
    if guess > st.session_state.number:
        st.write('Too high! Try again')
    elif guess < st.session_state.number:
        st.write('Too low! Try again')
    else:
        st.write('Well Done, ', name, '! You guessed it!')
        st.success('Congrats!')

# reset number with button
if st.button('🔄 Reset Number'):
    st.session_state.number = random.randint(1, 100)
    st.info("I've picked a new number — start guessing again!")
