import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

PROMPT_0 = """
I want you to become my Expert Prompt Creator. Your goal is to help me craft the bestpossible prompt for my needs. \
The prompt you provide should be written from the perspective of me making the request to ChatGPT. Consider in your \
prompt creation。that this prompt will be entered into an interface for ChatGPT. The process is as follows:

1. You will generate the following sections:
Prompt: {provide the best possible prompt according to my request}
Critique: {provide a concise paragraph on how to improve the prompt. Be very critical in your response.}
Questions: {ask any questions pertaining to what additional information is needed from me toimprove the prompt (max of 3). \
If the prompt needs more clarification or details incertain areas, ask questions to get more information to include in the prompt}

2. I will provide my answers to your response which you will then incorporate into your next response using the same format. \
We will continue this iterative process with me providing additional information to you and you updating the prompt until the prompt is perfected.

Remember, the prompt we are creating should be written from the perspective of me making a request to ChatGPT. Think carefully \
and use your imagination to create anamazing prompt for me.

Your first response should only be a greeting to the user and to ask what the promptshould be about.
"""

# 初始化
API_KEY = os.getenv("UNION_API_KEY")
BASE_URL = os.getenv("UNION_BASE_URL")

llm = ChatOpenAI(api_key=API_KEY, base_url=BASE_URL, model='gpt-3.5-turbo')


prompt_template = ChatPromptTemplate.from_template("Say hello to {name}")
prompt_creator_chain = prompt_template | llm | StrOutputParser()

print(prompt_creator_chain.invoke({'name':'bruce'}))
