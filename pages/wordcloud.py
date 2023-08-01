import streamlit as st
from utils import *

st.header("Wordcloud from news catgories")
fig = wordcloud()
st.pyplot(fig)