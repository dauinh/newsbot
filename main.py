from utils import *
import streamlit as st
from streamlit_tags import st_tags

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings()

@st.cache_data()
def load_faiss_index():
    file = "news_articles181"
    db = FAISS.load_local(file, embeddings)
    return db


db = load_faiss_index()
st.title("News Recommendation System")
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
    res = db.similarity_search_with_score(parsed_preferences)

    st.header("Recommended articles")
    for art in res:
        doc, score = art
        st.caption(f"[{doc.metadata['title']}]({doc.metadata['url']})")

else:
    st.text("Please enter keywords to get recommended articles")