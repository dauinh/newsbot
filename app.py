import streamlit as st
from utils import *


# Streamlit app
st.title("Feature extractions from news articles")

st.header("Category graph")
st.text("Large nodes are news categories \
        \nSmall dark blue nodes are news articles \
        \nDark green nodes are articles that user has read \
        \nLight green nodes are articles that we recommend")
from category_graph import agraph

st.header("Tag graph")
st.text("Large nodes are news tags \
        \nSmall dark blue nodes are news articles")
from tag_graph import agraph

st.header("Wordcloud from news catgories")
fig = wordcloud()
st.pyplot(fig)
