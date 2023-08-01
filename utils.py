import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def wordcloud():
    articles_db = load_data("data/clean.json")
    text = []
    for article in articles_db:
        text.append(article["category"])
    res = ",".join(text)
    # Create and generate a word cloud image
    wordcloud = WordCloud().generate(res)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return fig


def load_data(filename: str):
    with open(filename, "r") as file:
        output = json.load(file)
    return output
