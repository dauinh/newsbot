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
    return history
    

@st.cache_data()
def get_user_history(num_articles):
    with open("data/clean188.json", "r") as file:
        input = json.load(file)
    history = get_k_articles(input, num_articles)
    res = []
    for art in history:
        res.append(art)
    return res


@st.cache_data()
def load_faiss_index():
    file = "news_articles181"
    db = FAISS.load_local(file, embeddings)
    return db


def from_summary(db):
    st.text("Search similiar articles according to user read history")
    history = get_user_history(5)
    st.header("User history")
    all_summaries = []
    all_urls = set()
    for art in history:
        st.caption(f"[{art['title']}]({art['url']})")
        st.caption(art['summary'])
        all_summaries.append(art['summary'])
        all_urls.add(art['url'])

    parsed_history = '; '.join(all_summaries)
    res = db.similarity_search_with_score(
        query=parsed_history,
        k=10,
    )

    st.header("Recommended articles")
    for art in res:
        doc, score = art
        if doc.metadata['url'] in all_urls: continue
        st.caption(f"[{doc.metadata['title']}]({doc.metadata['url']})")
        st.caption(f"Similarity score: {str(round(score, 3))}")
        st.caption(doc.page_content)


def main():
    db = load_faiss_index()

    st.title("News Recommendation System")
    from_summary(db)

if __name__ == "__main__":
    main()