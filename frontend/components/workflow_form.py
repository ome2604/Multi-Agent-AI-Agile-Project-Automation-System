import streamlit as st
if "conversation_history" in data:

    st.subheader("Conversation History")

    for item in data["conversation_history"]:

        if "role" in item:

            st.markdown(
                f"### {item['role'].upper()}"
            )

            st.write(item["message"])

            st.divider()

        else:

            st.markdown("### USER")

            st.write(item["user_input"])

            st.markdown("### AI RESPONSE")

            st.write(item["response"])

            st.divider()