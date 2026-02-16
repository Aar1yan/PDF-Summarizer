import streamlit as st
from utils import extract_text_from_pdf, summarize_text

# App Title
st.title("📄 Offline AI PDF Summarizer Tool")

st.write("Upload any PDF and get an AI-generated summary (No API Key Needed).")

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF File", type="pdf")

if uploaded_file:
    st.success("PDF Uploaded Successfully!")

    # Extract Text Button
    if st.button("Generate Summary"):

        st.info("Extracting text from PDF...")

        text = extract_text_from_pdf(uploaded_file)

        st.info("Summarizing using Offline AI Model...")

        summary = summarize_text(text)

        st.subheader("✨ Summary Output")
        st.write(summary)
