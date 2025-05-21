
def sidebar(st) -> None:
    """
    Creates the sidebar for the NetApp Escalation Analysis app.

    Parameters:
    None

    Returns:
    None
    """
    st.sidebar.title('NetApp Application')
    st.sidebar.markdown('Welcome to the NetApp app! ')
    st.sidebar.markdown('Select a page from the sidebar to get started:')
    st.sidebar.markdown('---')
    st.sidebar.markdown('**Pages**')
    page = st.sidebar.radio('Go to', ['Home'])
    st.sidebar.markdown('---')

    force_rebuild_cache = st.sidebar.checkbox("Force Rebuild Cache")

    return page, force_rebuild_cache
