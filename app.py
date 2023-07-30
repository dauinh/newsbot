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


articles = load_data("process.json")
text = []
for article in articles:
    text.append(article['category'])
res = ','.join(text)
fig = wordcloud(res)

# Streamlit app
st.title('Feature extractions from news headlines')
from agraph import return_value
st.pyplot(fig)