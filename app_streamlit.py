import streamlit as st
import requests

st.title("Virtual Writing Assistant")

# Input text area
text = st.text_area("Enter your text:")

# Task selection
task = st.selectbox("Choose a task:", ["grammar_correction", "style_enhancement", "tone_adjustment"])

# Button to process text
if st.button("Process Text"):
    response = requests.post(
        "http://localhost:8000/process_text/",
        json={"text": text, "task": task}
    )
    if response.status_code == 200:
        result = response.json()["result"]
        st.write("Result:", result)
    else:
        st.error("Error processing text.")

