# LangChain Single Agent System

Autonomous single-agent implementation built with LangChain, featuring tool calling, custom function execution, and reasoning loops (ReAct).

---

## Overview

1. **Learning & Experiments:** LangChain primitives, prompt templates, LLM integration, and tool binding documented in `notebooks/langchain_notes.ipynb`.
2. **Agent Application:** Runnable single-agent implementation with custom tools and memory.

---

## Structure

```text
02-langchain-single-agent/
├── notebooks/
│   ├── langchain_notes.ipynb
│   └── ENVIRONMENT_SETUP.md
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## Setup & Execution

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   export GOOGLE_API_KEY="your-api-key"
   export TAVILY_API_KEY="your-api-key"
   export WEATHERSTACK_API_KEY="your-api-key"
   
   ```

3. **Run the agent:**
   ```bash
   python app.py
   ```
