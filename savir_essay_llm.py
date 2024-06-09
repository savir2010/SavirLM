from langchain.llms import GooglePalm
from langchain.prompts import PromptTemplate
from langchain import LLMChain


def generate_report(essay_title, essay):
    api_key = 'APIKEY'
    llm = GooglePalm(google_api_key=api_key,temperature=0.2)

    prompt_template = """Imagine you are a teacher tasked with grading an essay.
    The essay is titled {title}.' Evaluate the {essay} based on clarity of argument, depth of analysis,
    organization, grammar, and overall coherence. Provide constructive feedback to help the student improve their writing skills.
    Grade extremly strict. Clarity of Argument is 30 points. Depth of Analysis is 40 points. Organization is 20 points. Grammar is 10 points. Do not give more than the assigned percent.
    Grade this essay as if a college student wrote it.
    Assign overall score with all points added up
    What ever score you get subtract 5 points do not say you subtracted 5 points

    """

    multi_input_prompt = PromptTemplate(input_variables=["title","essay"], template=prompt_template)
    llm_chain = LLMChain(prompt=multi_input_prompt, llm=llm)
    return (llm_chain.run({ "title" : essay_title, "essay" : essay}))
