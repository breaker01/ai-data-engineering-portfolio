
import os
import certifi
import requests
import streamlit as st

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub


st.set_page_config(
    page_title="Capital Weather AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("Capital Weather AI Assistant")
st.markdown("Search + Weather AI Agent using LangChain")

os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

def get_secret(name):
    try:
        return st.secrets.get(name) or os.getenv(name)
    except Exception:
        return os.getenv(name)


GEMINI_API_KEY = get_secret("GOOGLE_API_KEY")
TAVILY_API_KEY = get_secret("TAVILY_API_KEY")
WEATHERSTACK_API_KEY = get_secret("WEATHERSTACK_API_KEY")


@tool
def get_weather_data(city: str) -> str:
    """Fetch current weather information for a city."""

    if not WEATHERSTACK_API_KEY:
        return "Weatherstack API key is missing."

    try:
        response = requests.get(
            "https://api.weatherstack.com/current",
            params={
                "access_key": WEATHERSTACK_API_KEY,
                "query": city
            },
            timeout=15
        )

        response.raise_for_status()
        data = response.json()

        if "current" not in data:
            return f"Could not fetch weather data for {city}: {data.get('error', 'Unknown error')}"

        current = data["current"]

        return (
            f"City: {city}\n"
            f"Temperature: {current['temperature']}°C\n"
            f"Weather: {current['weather_descriptions'][0]}\n"
            f"Humidity: {current['humidity']}%"
        )

    except requests.RequestException as e:
        return f"Weather request failed: {str(e)}"


user_query = st.text_input(
    "Enter your query:",
    placeholder="Example: Find the capital of Morocco and its current weather"
)

if st.button("Run Agent"):
    if not user_query.strip():
        st.warning("Please enter a query.")

    elif not all([GEMINI_API_KEY, TAVILY_API_KEY, WEATHERSTACK_API_KEY]):
        st.error("One or more API keys are missing. Check Streamlit Secrets.")

    else:
        with st.spinner("Agent is thinking..."):
            try:
                search_tool = TavilySearchResults(
                    max_results=1,
                    tavily_api_key=TAVILY_API_KEY
                )

                tools = [search_tool, get_weather_data]

                model = ChatGoogleGenerativeAI(
                    model="gemini-1.5-flash",
                    google_api_key=GEMINI_API_KEY,
                    temperature=0
                )

                prompt = hub.pull("hwchase17/react")

                agent = create_react_agent(
                    llm=model,
                    tools=tools,
                    prompt=prompt
                )

                agent_executor = AgentExecutor(
                    agent=agent,
                    tools=tools,
                    verbose=True,
                    handle_parsing_errors=True,
                    max_iterations=5
                )

                response = agent_executor.invoke({
                    "input": user_query
                })

                st.success("Response Generated")
                st.markdown("### Final Response")
                st.write(response["output"])

            except Exception as e:
                st.error(f"Error: {str(e)}")
