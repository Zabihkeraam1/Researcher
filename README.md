# Researcher Multi-Agent System

A multi-agent AI system built with **CrewAI** that performs research and writing tasks using specialized AI agents. The system uses autonomous agents to gather information, analyze topics, and generate clear written content.

## 🚀 Features

- 🤖 **Multi-Agent Architecture**
  - Research agent for collecting and verifying information.
  - Writing agent for transforming research into readable content.

- 🔎 **Web Research**
  - Uses search tools to gather information from online sources.
  - Focuses on reliable and relevant information.

- ✍️ **AI-Powered Writing**
  - Converts research results into structured and easy-to-understand responses.

- 🔌 **LLM Integration**
  - Supports Hugging Face models through LiteLLM.
  - Flexible model configuration through environment variables.

- ⚙️ **Environment Configuration**
  - Uses `.env` files for API keys and model settings.

---

## 🛠️ Technologies Used

- [CrewAI](https://github.com/crewAIInc/crewAI) - Multi-agent AI framework
- [CrewAI Tools](https://github.com/crewAIInc/crewAI-tools) - Agent tools and integrations
- [LiteLLM](https://github.com/BerriAI/litellm) - Unified LLM API interface
- [Hugging Face](https://huggingface.co/) - Open-source language models
- Python 3.12+
- uv - Fast Python package manager

---

## 📋 Requirements

- Python >= 3.12
- Hugging Face API token
- Search API key (for web research)

---

## ⚡ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Zabihkeraam1/Researcher.git
cd Researcher



uv sync


MODEL_NAME=huggingface/meta-llama/Llama-3.1-8B-Instruct
HF_TOKEN=your_huggingface_token
SERPER_API_KEY=your_serper_api_key

uv run main.py


Enter a topic: Who is Alan Turing?


Researcher-Multi-Agent/
│
├── main.py              # Application entry point
├── agents.py            # Agent definitions
├── tasks.py             # Task definitions
├── crew.py              # Crew orchestration
├── pyproject.toml       # Project configuration
├── .env                 # Environment variables
├── README.md            # Documentation
└── uv.lock              # Dependency lock file
