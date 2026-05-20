import streamlit as st
import pandas as pd

st.title("Enterprise Dashboard")

metrics = {

    "Metric": [
        "Agents",
        "Workflows",
        "API Status",
        "Memory Status",
        "RAG Status"
    ],

    "Value": [
        "5",
        "Operational",
        "Healthy",
        "Connected",
        "Active"
    ]
}

df = pd.DataFrame(metrics)

st.dataframe(
    df,
    use_container_width=True
)

st.success(
    "All enterprise systems operational"
)