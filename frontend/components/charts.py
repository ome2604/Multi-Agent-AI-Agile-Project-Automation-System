import streamlit as st
import pandas as pd
import plotly.express as px


def render_chart():

    data = pd.DataFrame({

        "Agent": [
            "Planning",
            "Risk",
            "Resource",
            "Scrum",
            "Report"
        ],

        "Latency": [
            10,
            7,
            5,
            6,
            8
        ]
    })

    fig = px.bar(
        data,
        x="Agent",
        y="Latency",
        title="Agent Latency"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )