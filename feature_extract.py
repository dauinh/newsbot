from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

from dotenv import load_dotenv
import json

load_dotenv()

template = """
You're a information mining system. Lets carefully extract information from this article

```{article}```

Step 1: Summarize given article
Step 2: Classify article from following categories: ```{categories}```
Step 3: Tag relevant topics. each topic should not be 1-2 words and cannot be more than 3 words, without abbreviation.
Step 4: Return the results in JSON format below:
{{ "category": category, "topics": [topics], "summary": summary }}
Summary is in less than 60 words
"""

CATEGORIES = "Politics, Business, Technology, Entertainment, Sports, Health, Science, World News, Environment, Education, Crime, Weather, Travel, Food, Lifestyle, Arts, Fashion, Automotive, Real Estate, Personal Finance"

prompt = PromptTemplate(template=template, input_variables=["article", "categories"])

model = OpenAI(
    model_name="text-davinci-002", 
    temperature=0,
    # max_tokens=100,
    streaming=True,
)

llm_chain = LLMChain(llm=model, prompt=prompt)

file_path = "data.json"

with open(file_path, "r") as file:
    data = json.load(file)
content = data[3]['body']

generated = llm_chain.run(article=content, categories=CATEGORIES)
print(generated)