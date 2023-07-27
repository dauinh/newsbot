from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.output_parsers import PydanticOutputParser

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

model = ChatOpenAI(
    model_name="gpt-3.5-turbo-16k-0613", 
    temperature=0,
    # max_tokens=100,
    streaming=True,
)

llm_chain = LLMChain(llm=model, prompt=prompt)
output_parser = PydanticOutputParser(pydantic_object=dict)

raw_data = "data.json"
processed_data = "processed.json"

# Load dataset
with open(raw_data, "r") as file:
    input = json.load(file)
with open(processed_data, "r") as file:
    output = json.load(file)

# Run LLM
for i, article in enumerate(input):
    if i > 25: break
    content = article['body']
    res = llm_chain.run(article=content, categories=CATEGORIES)
    parsed_output = json.loads(res)
    output.append(parsed_output)

# Write to JSON file
with open(processed_data, "w") as file:
    json.dump(output, file, indent=4)