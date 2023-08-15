from utils import *
import collections
import streamlit as st
from streamlit_agraph import Node, Edge, Config, agraph


articles_db = load_data("data/clean.json")
big_node_map = collections.defaultdict(list)
small2big = {}
nodes = []
edges = []


for article in articles_db:
    # Create URL nodes
    color="#7393B3"
    url_node = Node(
        id=article["url"],
        color=color,
        size=15,
    )
    nodes.append(url_node)

    # Create tags nodes
    for tag in article["tags"]:
        if tag not in big_node_map:
            tags_node = Node(
                id=tag,
                label=tag,
                size=25,
            )
            nodes.append(tags_node)
    
        # Organize urls into tags
        big_node_map[tag].append(article["url"])

        # Create URL-to-tags mapping
        small2big[article["url"]] = tag

        # Create edges from URL node to tags node
        edge = Edge(
            source=tag,
            target=article["url"],
        )
        edges.append(edge)
    


# user_profile = load_data("data/user.json")
# history = user_profile["readingHistory"]

# # Process user interested categories
# interested = []
# for read in history:
#     if read in small2big:
#         tags = small2big[read]
#         interested.append(tags)

# # Recommend articles
# rec_list = []
# for c in interested:
#     rec_list.extend(big_node_map[c])

# # Remove articles that user have read
# output = []
# for article in rec_list:
#     if article not in history:
#         output.append(article)


# # Create dictionaries for faster lookup
# history_dict = {read: True for read in history}
# output_dict = {rec: True for rec in output}


# for article in articles_db:
#     # Create URL nodes
#     if article["url"] in history_dict:
#         color="#2b5e4b"
#     elif article["url"] in output_dict:
#         color="#ACDBC9"
#     else:
    # color="#7393B3"
    # url_node = Node(
    #     id=article["url"],
    #     color=color,
    #     size=15,
    # )
    # nodes.append(url_node)
    
    # # Create edges from URL node to tags node
    # edge = Edge(
    #     source=article["tags"],
    #     target=url_node.id,
    # )
    # edges.append(edge)

config = Config(
    width=1600,
    height=1000,
    directed=True,
    physics=True,
    hierarchical=False,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",
)


st.title("Tag graph")
st.text("Large nodes are news tags \
        \nSmall dark blue nodes are news articles")

agraph(nodes=nodes, edges=edges, config=config)