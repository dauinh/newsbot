from utils import *
import collections
from streamlit_agraph import Node, Edge, Config, agraph


articles_db = load_data("data/clean.json")
big_node_map = collections.defaultdict(set)
small2big = {}
nodes = []
edges = []


for article in articles_db:
    cur = article["category"]
    # Create category nodes
    if cur not in big_node_map:
        category_node = Node(
            id=article["category"],
            label=article["category"],
            size=25,
        )
        nodes.append(category_node)
    
    # Organize urls into categories
    big_node_map[cur].add(article["url"])

    # Create URL-to-category mapping
    small2big[article["url"]] = cur


user_profile = load_data("data/user.json")
history = user_profile["readingHistory"]

# Process user interested categories
interested = []
for read in history:
    if read in small2big:
        category = small2big[read]
        interested.append(category)

# Recommend articles
rec_list = []
for c in interested:
    rec_list.extend(big_node_map[c])

# Remove articles that user have read
output = []
for article in rec_list:
    if article not in history:
        output.append(article)


# Create dictionaries for faster lookup
history_dict = {read: True for read in history}
output_dict = {rec: True for rec in output}


for article in articles_db:
    # Create URL nodes
    if article["url"] in history_dict:
        color="#2b5e4b"
    elif article["url"] in output_dict:
        color="#ACDBC9"
    else:
        color="#7393B3"
    url_node = Node(
        id=article["url"],
        color=color,
        size=15,
    )
    nodes.append(url_node)
    
    # Create edges from URL node to category node
    edge = Edge(
        source=article["category"],
        target=url_node.id,
    )
    edges.append(edge)

config = Config(
    width=1600,
    height=1000,
    directed=True,
    physics=True,
    hierarchical=False,
    nodeHighlightBehavior=True,
    highlightColor="#F7A7A6",
)

agraph(nodes=nodes, edges=edges, config=config)