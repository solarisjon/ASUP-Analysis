import streamlit as st
from components.netapp_page import netapp_markdown

st.set_page_config(page_title='NetApp ASUP Views',
                   layout='wide')

st.logo("components/netapp_logo.png", 
        icon_image="components/netapp_logo.png")


uploaded_files = st.sidebar.file_uploader("Choose text files", 
                                          type=None, 
                                          accept_multiple_files=False)

if uploaded_files is not None:
    # Read the contents of the uploaded file
    file_contents = uploaded_files.read()
    # Decode the bytes to a string
    file_contents = file_contents.decode('utf-8')
    # Store the contents in session state
    print(file_contents)
    st.session_state['uploaded_data'] = file_contents


netapp_markdown(st)




