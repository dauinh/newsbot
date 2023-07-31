import streamlit as st

from utils import *
from streamlit_agraph import agraph
from agraph import nodes, edges, config


articles = load_data("process.json")
text = []
for article in articles:
    text.append(article['category'])
res = ','.join(text)
fig = wordcloud(res)

# Streamlit app
st.title('Feature extractions from news headlines')
agraph(nodes=nodes, edges=edges, config=config)
st.pyplot(fig)