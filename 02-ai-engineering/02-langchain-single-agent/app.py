import os, certifi, requests
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from langchain_classic.agents import create_react_agent, AgentExecutor

from langsmith import Client

import streamlit as st


client = Client()

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv("/home/med/datacamp/ai-data-engineering-portfolio/02-ai-engineering/02-langchain-single-agent/notebooks/.env")

GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
WEATHERSTACK_API_KEY = os.getenv('WEATHERSTACK_API_KEY')


search_tool = TavilySearchResults(max_results=1)

result_search = search_tool.invoke('What is the capital of Morocco ?')
# print(result_search)
@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information for a city.
    """

    url = (
        f"https://api.weatherstack.com/current?"
        f"access_key={WEATHERSTACK_API_KEY}&query={city}"
    )

    response = requests.get(url)

    data = response.json()

    if "current" not in data:
        return f"Could not fetch weather data for {city}"

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%")
    
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=GEMINI_API_KEY,
)

# result = model.invoke("How much is 5x5 ?")
# print(result.text)


prompt = client.pull_prompt('hwchase17/react',dangerously_pull_public_prompt=True)

tools = [search_tool]

agent = create_react_agent(llm=model,tools=tools,prompt=prompt)

agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True,
                               handle_parsing_errors=True)
# # agent_executor
# response = agent_executor.invoke({"input":("find the capital of morocco"
#                                            "and then get its current wheater")})
# print(response["output"])

st.set_page_config(page_title="Agentic AI Assitant",page_icon="🤖",layout="centered")

st.title= ("Agentic AI Assitant")
st.markdown("Search + Weather AI Agent using langchain")

user_query = st.text_input("Enter your query:",placeholder="Example: find the capital and weather of city X")

if st.button("Run Agent:"):
    if user_query:
        with st.spinner('Agent is thinking..'):
            try:
                response = agent_executor.invoke({"input":(user_query)})
                st.success("Response Generated")
                st.markdown("## Final Response")
                st.write(response["output"])
            except Exception as e:
                st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a query")