# LangGraph

This repository contains all the experiments done to explore Langgraph and it's concepts

# LangGraph Exploration

This project explores the use of LangGraph for building AI agents. It provides a basic example of how to create and run agents using LangGraph and LangChain.

## Setup

### Using Conda to create a virtual environment

1. Create a new conda environment:

   ```bash
   conda create -n langgraph python=3.12
   conda activate langgraph
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

## Environment Variables

Create a `.env` file in the root directory with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

## Running the Example

The project includes a basic agent example in `langgraph/basic_agent.py`. To run it:

```bash
# Using Poetry
poetry run python langgraph/basic_agent.py

# Using Conda
python langgraph/basic_agent.py
```
