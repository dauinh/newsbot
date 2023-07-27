import streamlit as st
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'
def load_data():
    processed_data = "processed.json"
    with open(processed_data, "r") as file:
        output = json.load(file)
    return output

def wordcloud(text):
    # Create and generate a word cloud image
    wordcloud = WordCloud().generate(text)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    return fig


data = load_data()
text = []
for article in data:
    text.append(article['category'])
res = ','.join(text)
fig = wordcloud(res)

# Streamlit app
st.title('Feature extractions from news headlines')
st.pyplot(fig)