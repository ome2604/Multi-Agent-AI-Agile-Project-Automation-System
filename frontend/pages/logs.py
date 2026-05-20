import streamlit as st

st.title("System Logs")

try:

    with open("logs/system.log", "r") as file:

        logs = file.read()

    st.text_area(
        "Execution Logs",
        logs,
        height=600
    )

except Exception:

    st.warning(
        "No logs found"
    )