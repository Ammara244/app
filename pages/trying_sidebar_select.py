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


st.title("Data Analysis")

with st.expander("Data Overview"):
    st.write("Summary of dataset...")
    st.write("Shape, columns, etc.")

with st.expander("Data Cleaning"):
    st.write("Missing values, duplicates...")

with st.expander("Visualization"):
    st.write("Charts and graphs...")
