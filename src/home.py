import streamlit as st
from icecream import ic
from io import BytesIO


def save_plot_to_buffer(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return buf

def home_page(force_cache_reload: bool):
    st.title('Home Page')
