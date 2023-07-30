import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from utils import *


text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

def wordcloud(text):
    # Create and generate a word cloud image
    wordcloud = WordCloud().generate(text)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    return fig


articles = load_data("processed.json")
text = []
for article in articles:
    text.append(article['category'])
res = ','.join(text)
fig = wordcloud(res)

from streamlit_agraph import agraph
from agraph import nodes, edges, config

from rec import history, output

for n in nodes:
    for read in history:
        if n.id == read:
            n.color = "#2b5e4b"
    for rec in output:
        if n.id == rec:
            n.color = "#ACDBC9"

# Streamlit app
st.title('Feature extractions from news headlines')
agraph(nodes=nodes, edges=edges, config=config)
st.pyplot(fig)