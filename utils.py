import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud(text):
    # Create and generate a word cloud image
    wordcloud = WordCloud().generate(text)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    return fig

def load_data(filename: str):
    with open(filename, "r") as file:
        output = json.load(file)
    return output