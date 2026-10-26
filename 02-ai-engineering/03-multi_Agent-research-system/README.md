# LangChain Multi-Agent Research System

An autonomous multi-agent research and analysis system built with LangChain, LangGraph, and modern LLM tool-calling capabilities.

---

## Project Overview

This project implements a collaborative multi-agent architecture to conduct research, synthesize information, and produce reports. Instead of relying on a single monolithic prompt, multiple specialized agents collaborate under a supervisor/orchestrator:

- **Supervisor / Orchestrator Agent**: Breaks down user research queries, decides task delegations, routes requests, and synthesizes final outputs.
- **Web Research Agent**: Uses web search tools (e.g., Tavily Search) to gather up-to-date facts, references, and sources.
- **Analysis / Writer Agent**: Analyzes gathered data, summarizes key points, and drafts structured, cited research documents.
- **Chart / Code Agent (Optional)**: Generates visualizations, charts, or runs Python code to verify data when applicable.

---

## Architecture

```
                       ┌─────────────────────────┐
                       │     User Research       │
                       │         Query           │
                       └────────────┬────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                 ┌────►│   Supervisor Agent      │◄────┐
                 │     │ (Routing & Delegation)  │     │
                 │     └──────┬───────────┬──────┘     │
                 │            │           │            │
                 │            ▼           ▼            │
         Findings│    ┌──────────────┐  ┌────────────┐ │ Findings
                 └────┤Web Researcher│  │Chart/Code  ├─┘
                      │    Agent     │  │   Agent    │
                      └──────────────┘  └────────────┘
```

---

## Tech Stack & Key Concepts

- **Framework:** LangChain & LangGraph
- **LLM:** Google Gemini (`gemini-flash-latest`) / OpenAI
- **Search Tool:** Tavily Search API
- **State Management:** LangGraph `StateGraph` / `MessagesState`
- **Pattern:** Supervisor-Worker Multi-Agent Workflow

---

## Project Structure

```
03-multi_Agent-research-system/
├── README.md               # Project documentation and architecture overview
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variable template
└── notebooks/              # Exploration and step-by-step walkthroughs
    └── multi_agent_demo.ipynb
```

---

## Getting Started

### 1. Environment Setup

Create and activate a virtual environment:
```bash
conda create -n multi-agent python=3.11 -y
conda activate multi-agent
```

Install requirements:
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file with your API keys:
```env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
# Optional:
LANGSMITH_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
```

---

## Roadmap & Milestones

- [x] Step 1: Initialize project documentation & design architecture.
- [ ] Step 2: Set up environment and dependencies (`requirements.txt`).
- [ ] Step 3: Implement individual specialized worker tools and agents.
- [ ] Step 4: Build supervisor graph orchestration with LangGraph.
- [ ] Step 5: Test end-to-end research query workflows and output verification.
