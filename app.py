import streamlit as st
from utils import *


# Streamlit app
st.title("Feature extractions from news articles")

from category_graph import agraph

fig = wordcloud()
st.pyplot(fig)
