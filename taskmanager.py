import os
import getpass

from langchain_google_community import CalendarToolkit
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent

# Set Google Gemini API key or other LLM API key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google Gemini API key: ")

# Initialize the chat model 
llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


toolkit = CalendarToolkit()  # reads credentials.json by default

# Get all the calendar tools
tools = toolkit.get_tools()

# Create the AI agent with the LLM and calendar tools
agent_executor = create_react_agent(llm, tools)

print("AI Agent is ready! Type your commands:")

while True:
    query = input("User: ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Pass user query 
    events = agent_executor.stream(
        {"messages": [("user", query)]},
        stream_mode="values",
    )

    # Print AI responses
    for event in events:
        event["messages"][-1].pretty_print()

