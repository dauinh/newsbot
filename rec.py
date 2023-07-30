import collections
from utils import *


articles_db = load_data("processed.json")
category_map = collections.defaultdict(set)
url2category = {}

# Organize urls into categories
for article in articles_db:
    cur = article['category']
    category_map[cur].add(article['url'])

for i, article in enumerate(articles_db):
    category = article['category']
    url = article['url']
    url2category[url] = category

user_profile = load_data("user.json")
history = user_profile['readingHistory']
history = set(history)

# Process user interested categories
interested = set()
for read in history:
    category = url2category[read]
    interested.add(category)

# Recommend articles
rec_list = []
for c in interested:
    rec_list.extend(category_map[c])

# Remove articles that user have read
output = []
for article in rec_list:
    if article not in history:
        output.append(article)
