import streamlit as st

subpage = st.sidebar.selectbox("Choose a section (you coud do this for options of different pages within a page)", ["one", "two", "three"])

if subpage == "one":
    st.header(" first choice")
    st.write("this comes up")

elif subpage == "two":
    st.header("second choice")
    st.write("this comes up as second")

elif subpage == "three":
    st.header("third choice")
    st.write("this comes up as third.")


st.write('or you coud do this for options of different pages within a page')

with st.expander("Data Overview"):
    st.write("Summary of dataset...")
    st.write("Shape, columns, etc.")

with st.expander("Data Cleaning"):
    st.write("Missing values, duplicates...")

with st.expander("Visualization"):
    st.write("Charts and graphs...")
