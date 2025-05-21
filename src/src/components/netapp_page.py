# Set the color theme
#import streamlit as st

def netapp_markdown(st):

    st.markdown(
        """
        <style>
        .css-18e3th9 {
            background-color: #0067C5;  /* NetApp blue */
        }
        .css-1d391kg {
            background-color: #0067C5;  /* NetApp blue */
        }
        .css-1v3fvcr {
            color: white;
        }
        .css-145kmo2 {
            color: white;
        }
        .css-1cpxqw2 {
            color: white;
        }
        .css-1inwz65 {
            color: white;
        }
        .css-1r6slb0 {
            color: white;
        }
        .css-1a32fsj {
            color: white;
        }
        footer {
            visibility: hidden;
        }
        .footer {
            visibility: visible;
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #0067C5;
            color: white;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            <p>Created by Jon Bowman</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add NetApp logo at the top of the sidebar
    st.sidebar.image("src/components/netapp_logo.png", use_container_width=True)