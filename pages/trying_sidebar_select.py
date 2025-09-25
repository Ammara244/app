import streamlit as st

subpage = st.sidebar.selectbox("Choose a section", ["one", "two", "three"])

if subpage == "one":
    st.header(" first choice")
    st.write("this comes up")

elif subpage == "two":
    st.header("second choice")
    st.write("this comes up as second")

elif subpage == "three":
    st.header("third choice")
    st.write("this comes up as third.")
