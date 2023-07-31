import json
from eventregistry import *
from dotenv import load_dotenv

load_dotenv()
topics_dist = {
    "business": 19,
    "sports": 5,
    "entertainment": 11,
    "technology": 15,
    "health": 13,
    "politics": 6,
    "science": 10,
    "weather": 4,
    "travel": 11,
    "education": 6,
}


def get_articles(er: EventRegistry, category: str, n: int):
    category_uri = er.getCategoryUri(category)

    q = QueryArticlesIter(categoryUri=category_uri)

    res = q.execQuery(er, sortBy="date", maxItems=n)

    # File path to save the JSON data
    file_path = "data/test.raw.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    for art in res:
        if not art['isDuplicate']:
            data.append(art)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    er = EventRegistry(apiKey=os.environ.get("NEWSAPI_KEY"), allowUseOfArchive=False)
    for topic, count in topics_dist.items():
        get_articles(er, topic, count)
    