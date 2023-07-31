import streamlit as st

from utils import *
from streamlit_agraph import agraph
from agraph import nodes, edges, config

# Wordcloud
articles = load_data("data/test.json")
text = []
for article in articles:
    text.append(article["category"])
res = ",".join(text)
fig = wordcloud(res)

# Category graph
from rec import history, output

for n in nodes:
    for read in history:
        if n.id == read:
            n.color = "#2b5e4b"
    for rec in output:
        if n.id == rec:
            n.color = "#ACDBC9"

# Streamlit app
st.title("Feature extractions from news articles")
agraph(nodes=nodes, edges=edges, config=config)
st.pyplot(fig)
