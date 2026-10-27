from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import web_search,scrape_url
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')

# model initialization
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=GEMINI_API_KEY,
    temperature=0,
    max_retries=2,
)

SEARCH_SYSTEM_PROMPT = """You are an expert research discovery agent.
Search the web for the requested topic. 
CRITICAL REQUIREMENT:
You MUST explicitly list all source URLs and their titles in your final response under a 'Sources' section so that downstream scraping agents can visit and scrape them. Never omit the URLs."""

# Search Agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt=SEARCH_SYSTEM_PROMPT
    )
    
#reader agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url],
    )

writer_prompt = ChatPromptTemplate.from_messages([
    ("system","You are an Expert research writer. Write clear, structured and insightful reports."),
    ("human","""Write a detailed research report on the topic below.
     
Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional
     """),
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain 
critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()