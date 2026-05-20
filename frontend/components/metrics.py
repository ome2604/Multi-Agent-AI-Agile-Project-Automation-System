import streamlit as st


def render_metrics():

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Agents",
        "5"
    )

    col2.metric(
        "Latency",
        "2.1s"
    )

    col3.metric(
        "Status",
        "Healthy"
    )