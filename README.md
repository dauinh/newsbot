# newsrec
A news recommendation system

[Streamlit demo included](https://newsrec.streamlit.app/)

> If demo doesn’t work, it’s probably because the Streamlit account doesn’t exist anymore

Virutal environments recommended

```
pip install -r requirements.txt
```

### Scrape news data

[NewsAPI](https://newsapi.org/) is used to scrape news data. This API gives details of articles from URL, language, publish dates and time, scrape date and time, title, article content, news source, authors and images. However, most articles are from questionable sources and there are duplicates with different URLs.

### Extract article information

Extract information from each article using GPT model and [LangChain](https://python.langchain.com/).

### News Recommendation

#### Graph search
- Category graph
- Tag graph

#### Vector search
- By keyword 
- By summary 