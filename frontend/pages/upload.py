import streamlit as st
from pathlib import Path

st.title("Document Upload")

uploaded_file = st.file_uploader(

    "Upload Documents",

    type=["pdf", "txt", "docx"]
)

if uploaded_file:

    upload_dir = Path("documents")

    upload_dir.mkdir(
        exist_ok=True
    )

    file_path = upload_dir / uploaded_file.name

    with open(file_path, "wb") as file:

        file.write(
            uploaded_file.read()
        )

    st.success(
        f"{uploaded_file.name} uploaded successfully"
    )

    st.info(
        "Document ready for RAG ingestion"
    )