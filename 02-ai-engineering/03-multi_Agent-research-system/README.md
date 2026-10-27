# LangChain Multi-Agent Research System

Autonomous 4-stage multi-agent research and synthesis engine built with LangChain, Google Gemini, Tavily, Trafilatura, and Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://theresearcher.streamlit.app/)
🌐 **Live Demo:** [https://theresearcher.streamlit.app/](https://theresearcher.streamlit.app/)

---

## Project Overview

This project implements a collaborative multi-agent architecture designed to automate deep research, web content extraction, report drafting, and objective evaluation. Instead of relying on a single monolithic prompt, four specialized stages collaborate in sequence:

1. **Search Agent:** Uses the Tavily Search API to identify high-authority sources, discovering key insights while retaining source URLs and page titles.
2. **Reader Agent:** A dedicated scraping agent equipped with resilient multi-strategy extraction (`trafilatura` for clean article parsing, falling back to `readability-lxml` + `BeautifulSoup`).
3. **Writer Chain:** Synthesizes aggregated search summaries and deep scraped content into a professional, structured document (Introduction, Key Findings, Conclusion, Sources).
4. **Critic Chain:** Performs an objective rubric-based evaluation of the report, issuing an empirical score ($X/10$), identifying strengths, highlighting areas for improvement, and providing a final verdict.

---

## Architecture

```
                       ┌─────────────────────────┐
                       │   User Research Topic   │
                       └────────────┬────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │  Step 1: Search Agent   │
                       │   (Tavily Search API)   │
                       └────────────┬────────────┘
                                    │ Sources & URLs
                                    ▼
                       ┌─────────────────────────┐
                       │  Step 2: Reader Agent   │
                       │ (Trafilatura / Scraper) │
                       └────────────┬────────────┘
                                    │ Deep Content & Findings
                                    ▼
                       ┌─────────────────────────┐
                       │  Step 3: Writer Chain   │
                       │  (Structured Synthesis) │
                       └────────────┬────────────┘
                                    │ Drafted Report
                                    ▼
                       ┌─────────────────────────┐
                       │  Step 4: Critic Chain   │
                       │ (Rubric & Score Review) │
                       └────────────┬────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │   Interactive Web UI    │
                       │       (Streamlit)       │
                       └─────────────────────────┘
```

---

## Tech Stack & Key Concepts

- **Framework:** LangChain & LangChain Google GenAI
- **LLM:** Google Gemini (`gemini-3.5-flash-lite`)
- **Search Tool:** Tavily Search API
- **Web Extraction:** Trafilatura, Readability-lxml, BeautifulSoup4
- **UI & Presentation:** Streamlit (Custom Cyberpunk / Slate Theme)
- **Design Pattern:** Sequential Multi-Agent Pipeline with LCEL Chains

---

## Project Structure

```text
03-multi_Agent-research-system/
├── app.py                  # Interactive Streamlit application & UI
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation and architecture overview
└── src/
    ├── __init__.py
    ├── tools/
    │   ├── __init__.py
    │   └── tools.py        # Tavily search & resilient multi-strategy web scraper
    ├── agents/
    │   ├── __init__.py
    │   └── agents.py       # Search & Reader agents, Writer & Critic LCEL chains
    └── pipeline/
        ├── __init__.py
        └── pipeline.py     # Deterministic 4-step pipeline orchestration
```

---

## Setup & Local Execution

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

Create a `.env` file in this directory with your API keys:
```env
GOOGLE_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Run the Application

Launch the Streamlit interface:
```bash
streamlit run app.py
```

Or run the pipeline via CLI:
```bash
python -m src.pipeline.pipeline
```

---

## Roadmap & Milestones

- [x] Step 1: Design multi-agent sequential architecture and tool specifications.
- [x] Step 2: Set up environment and dependencies (`requirements.txt`).
- [x] Step 3: Implement specialized tools (Tavily search & Trafilatura scraper).
- [x] Step 4: Implement specialized agents (`search_agent`, `reader_agent`) and LCEL chains (`writer_chain`, `critic_chain`).
- [x] Step 5: Build interactive Streamlit dashboard with custom CSS styling and real-time step visualization.
- [x] Step 6: Deploy live to Streamlit Community Cloud.
