

def netapp_markdown(st):

    st.logo("components/netapp_logo.png", 
            icon_image="components/netapp_logo.png",
            size="large")
    
    st.sidebar.markdown('---')
    st.sidebar.markdown('**Contact**: For any questions or feedback, please contact jon.bowman@netapp.com.')
    st.sidebar.markdown('---')
    

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
            <p>This app is for internal use only and should not be shared outside of NetApp.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
