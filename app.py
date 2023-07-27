import streamlit as st

st.title('Feature extractions from news headlines')

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create some sample text
text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image
wordcloud = WordCloud().generate(text)
fig, ax = plt.subplots()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(fig)