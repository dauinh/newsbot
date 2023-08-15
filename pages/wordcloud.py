import streamlit as st
from utils import *

st.title("Wordcloud from news catgories")
fig = wordcloud()
st.pyplot(fig)