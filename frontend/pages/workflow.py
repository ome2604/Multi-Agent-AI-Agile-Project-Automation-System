import streamlit as st

from services.api_client import (
    login,
    execute_workflow
)

st.title("Workflow Execution")

username = st.text_input(
    "Username",
    value="admin"
)

password = st.text_input(
    "Password",
    type="password",
    value="admin"
)

goal = st.text_area(
    "Project Goal",
    height=200
)

if st.button("Execute Workflow"):

    with st.spinner("Authenticating..."):

        auth = login(
            username,
            password
        )

    token = auth["access_token"]

    with st.spinner("Running Enterprise Workflow..."):

        result = execute_workflow(
            goal,
            token
        )

    # =========================
    # ERROR HANDLING
    # =========================

    if result.get("status") == "failed":

        st.error(
            result.get("error")
        )

    else:

        st.success("Workflow Completed")

        data = result["data"]

        st.subheader("Planning Output")
        st.write(data.get("plan"))

        st.subheader("Risk Analysis")
        st.write(data.get("risks"))

        st.subheader("Resource Allocation")
        st.write(data.get("resources"))

        st.subheader("Scrum Updates")
        st.write(data.get("scrum"))

        st.subheader("Final Report")
        st.write(data.get("report"))