# crew_AI

This is a sample project built with CrewAI, originally created in Google Colab.

## Prerequisites

- Python 3.9 or later
- `pip` installed
- API keys for:
  - [Serper](https://serper.dev/) (`SERPER_API_KEY`)
  - [Google AI Studio / Gemini](https://aistudio.google.com/app/apikey) (`GEMINI_API_KEY`)

Install the required packages:

```bash
pip install gradio crewai crewai_tools
```

If you want to use a `.env` file, also install:

```bash
pip install python-dotenv
```

## Setup

The app reads API keys from environment variables:

- `SERPER_API_KEY` — for the Serper web search tool
- `GEMINI_API_KEY` — for the Gemini model used by the agents

### Run locally

```bash
export SERPER_API_KEY="your_serper_key"
export GEMINI_API_KEY="your_gemini_key"
python3 crew_ai.py
```

### Optional: use a `.env` file

You can also put the keys in a `.env` file in the project root:

```env
SERPER_API_KEY=your_serper_key
GEMINI_API_KEY=your_gemini_key
```

Install [python-dotenv](https://pypi.org/project/python-dotenv/) and the app will load the file automatically on startup:

```bash
pip install python-dotenv
python3 crew_ai.py
```
