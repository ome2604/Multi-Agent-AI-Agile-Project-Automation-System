import streamlit as st

from components.sidebar import render_sidebar

st.set_page_config(

    page_title="Enterprise AI Platform",

    layout="wide"
)

render_sidebar()

st.title("Enterprise Multi-Agent AI Platform")

st.markdown("""
Welcome to the Enterprise AI Workflow Dashboard
""")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Agents",
    "5"
)

col2.metric(
    "Workflow Status",
    "Running"
)

col3.metric(
    "System Health",
    "Healthy"
)

st.success(
    "Enterprise AI Platform Running Successfully"
)