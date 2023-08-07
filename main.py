from utils import *
import streamlit as st
from streamlit_tags import st_tags

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

def get_k_articles(data, k):
    """Randomly choose k articles as user reading history"""
    import random

    indices = random.sample(range(1, len(data)), k)
    history = []
    for i in indices:
        history.append(data[i])


@st.cache_data()
def get_user_history(num_articles):
    with open("data/clean188.json", "r") as file:
        input = json.load(file)
    history = get_k_articles(input, num_articles)
    res = []
    for art in history:
        res.append(art['summary'])
    return '; '.join(res)


@st.cache_data()
def load_faiss_index():
    file = "news_articles181"
    db = FAISS.load_local(file, embeddings)
    return db


def from_keywords(db):
    st.text("Search similiar articles according to preferences")
    keywords = st_tags(
        label='## Enter Preferences:',
        text='Press enter to add more',
        value=['business', 'network'],
        suggestions=[],
        maxtags = 5,
        key='1')

    if keywords:
        parsed_preferences = '; '.join(keywords)
        res = db.similarity_search_with_score(
            query=parsed_preferences,
            k=5,
        )

        st.header("Recommended articles")
        for art in res:
            doc, score = art
            st.caption(f"[{doc.metadata['title']}]({doc.metadata['url']})")
            st.caption(f"Similarity score: {str(round(score, 3))}")
            st.caption(doc.page_content)

    else:
        st.text("Please enter keywords to get recommended articles")


def main():
    db = load_faiss_index()
    # history = get_user_history(5)

    st.title("News Recommendation System")
    from_keywords(db)


if __name__ == "__main__":
    main()