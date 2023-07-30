import json
from collections import defaultdict
import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
categories = set()
topic_set = set()

processed_data = "processed.json"

# Load dataset
with open(processed_data, "r") as file:
    data = json.load(file)

for i, article in enumerate(data):
    # if i > 5: break
    if article['category'] in categories: continue
    categories.add(article['category'])
    category_node = Node(id=article['category'], 
                   label=article['category'], 
                   size=25,
                )
    nodes.append(category_node)
    for topic in article['topics']:
        if topic in topic_set: continue
        topic_set.add(topic)
        topic_node = Node(id=topic,
                        size=15,
                        )
        nodes.append(topic_node)
        new_edge = Edge(source=category_node.id,
                        target=topic_node.id,
                   )
        edges.append(new_edge)

config = Config(width=1600,
                height=1000,
                directed=True, 
                physics=True, 
                hierarchical=False,
                nodeHighlightBehavior=True, 
                highlightColor="#F7A7A6",
                )

return_value = agraph(nodes=nodes, 
                      edges=edges,
                      config=config)