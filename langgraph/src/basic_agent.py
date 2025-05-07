from typing import Annotated, TypedDict
from langgraph.graph import Graph, StateGraph
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the state
class AgentState(TypedDict):
    messages: list[HumanMessage | AIMessage]
    next: str

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Define the nodes
def generate_response(state: AgentState) -> AgentState:
    """Generate a response using the LLM."""
    messages = state["messages"]
    response = llm.invoke(messages)
    state["messages"].append(response)
    state["next"] = "end"
    return state

def should_continue(state: AgentState) -> str:
    """Determine if the conversation should continue."""
    return state["next"]

# Create the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("generate", generate_response)

# Add edges
workflow.add_edge("generate", "end")

# Set the entry point
workflow.set_entry_point("generate")

# Compile the graph
app = workflow.compile()

def run_agent(user_input: str) -> str:
    """Run the agent with the given user input."""
    # Initialize the state
    state = {
        "messages": [HumanMessage(content=user_input)],
        "next": "generate"
    }
    
    # Run the graph
    result = app.invoke(state)
    
    # Return the last message
    return result["messages"][-1].content

if __name__ == "__main__":
    # Example usage
    user_input = "Hello, how are you?"
    response = run_agent(user_input)
    print(f"User: {user_input}")
    print(f"Agent: {response}") 