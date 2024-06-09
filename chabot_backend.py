from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch #for nlp
import pandas as pd
# from langchain import llms
from langchain_community.llms import Ollama
from ollama import generate
#from langchain_google_vertexai import VertexAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# response = generate('mistral', 'Why is the sky blue?')
# print(response['response'])

api_key = 'AIzaSyCWS8sL04uunSJIww-5KNEcS-h4jFYhal4'
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

def get_sentiment(text):
    tokens = tokenizer.encode(text,return_tensors='pt')
    result = model(tokens)
    sentiment = int(torch.argmax(result.logits))+1
    return sentiment

def respond(word_problem,context,sentiment):
    # api_key = 'AIzaSyBs2o10zydHsc-0ca4so1qpP--vwUsBvkE'
    llm = Ollama(model="llama2")

    prompt_template =  """Do not say the problemYou are a math tutor chatbot. Your role is to guide students through math problems without giving away the answers. Use the provided context and sentiment score (1-5) to tailor your response. 

- Sentiment 1: Very Negative
- Sentiment 2: Negative
- Sentiment 3: Neutral
- Sentiment 4: Positive
- Sentiment 5: Very Positive

ALWAYS CHECK IF THE USER HAS ANSWERED THE QUESTION THAT IS THE MOST IMPORTANT THING
Do not make up stuff act like a nice math tutor.
Remember you are a math tutor already you should be able to solve this problem and know the steps the user is not always right only sometimes.
Respond empathetically and constructively. Encourage the student to think critically and work through the problem step by step.
If the user is asking for how to solve the word problem give a step by step explanation how to get the answer
Always check is the user has answered the question.
{word_problem}
{context}
{sentiment}
"""

    multi_input_prompt = PromptTemplate(input_variables=["word_problem","context","sentiment"], template=prompt_template)
    llm_chain = multi_input_prompt | llm
    return (llm_chain.invoke({ "word_problem" :word_problem,"context":context, "sentiment" : sentiment}))

word_problem = "Sarah has 24 apples. She wants to divide them equally among her 4 friends. How many apples will each friend get?"
answer = "6"
context = "What is the next step for me to solve"
sentiment = str(get_sentiment(context))

print(respond(word_problem,context,sentiment))