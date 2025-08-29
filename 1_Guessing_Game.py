import streamlit as st
import random

st.title("🎲 Number Guessing Game")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)

guess = st.number_input("Enter your guess (1–100):", min_value=1, max_value=100)
if st.button("Check my guess"):
    if guess < st.session_state.number:
        st.write("Too low! Try again 👇")
    elif guess > st.session_state.number:
        st.write("Too high! Try again 👆")
    else:
        st.success("🎉 Correct! I picked a new number.")
        st.session_state.number = random.randint(1, 100)
