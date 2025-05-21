import streamlit as st

def colortext(st):
    st.markdown(
            """
            <style>
            .blue-text {
                color: blue;
                font-size: 20px;
                font-weight: bold;
            }
            .yello-text {
                color: yellow;
                font-size: 16px;
                font-style: italic;
            }
            </style>"
            """,
            unsafe_allow_html=True
        )
        