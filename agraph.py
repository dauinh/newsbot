from utils import *
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []
category_map = {}
article_set = set()

data = load_data("data/test.json")

for i, article in enumerate(data):
    if article["category"] in category_map:
        continue
    category_node = Node(
        id=article["category"],
        label=article["category"],
        size=25,
    )
    category_map[article["category"]] = category_node.id
    nodes.append(category_node)

for i, article in enumerate(data):
    # if i > 5: break
    # Add url nodes
    if article["url"] in article_set:
        continue
    article_set.add(article["url"])
    url_node = Node(
        id=article["url"],
        color="	#7393B3",
        size=15,
    )
    nodes.append(url_node)
    category_node_id = category_map[article["category"]]
    edge = Edge(
        source=category_node_id,
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

# return_value = agraph(nodes=nodes, edges=edges, config=config)
