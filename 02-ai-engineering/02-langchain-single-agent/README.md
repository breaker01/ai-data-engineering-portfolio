# LangChain Single Agent System

Autonomous single-agent implementation built with LangChain, featuring tool calling, custom function execution, and reasoning loops (ReAct).

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://capital-weather.streamlit.app/)
🌐 **Live Demo:** [https://capital-weather.streamlit.app/](https://capital-weather.streamlit.app/)

---

## Overview

1. **Learning & Experiments:** LangChain primitives, prompt templates, LLM integration, and tool binding documented in `notebooks/agent_demo.ipynb`.
2. **Agent Application:** Interactive Streamlit web interface (`app.py`) executing a ReAct agent equipped with search (Tavily) and live weather lookup (Weatherstack).

---

## Structure

```text
02-langchain-single-agent/
├── notebooks/
│   ├── agent_demo.ipynb
│   └── ENVIRONMENT_SETUP.md
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## Setup & Local Execution

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   Create a `.env` file or export the following API keys:
   ```bash
   export GOOGLE_API_KEY="your-gemini-api-key"
   export TAVILY_API_KEY="your-tavily-api-key"
   export WEATHERSTACK_API_KEY="your-weatherstack-api-key"
   ```

3. **Run the Streamlit application:**
   ```bash
   streamlit run app.py
   ```
