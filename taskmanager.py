import os
import getpass

from langchain_google_community import CalendarToolkit
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent

# Set Google Gemini API key or other LLM API key
if not os.environ.get("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google Gemini API key: ")


llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")


toolkit = CalendarToolkit()  


tools = toolkit.get_tools()


agent_executor = create_react_agent(llm, tools)

print("AI Agent is ready! Type your commands:")

while True:
    query = input("User: ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

 
    events = agent_executor.stream(
        {"messages": [("user", query)]},
        stream_mode="values",
    )

    
    for event in events:
        event["messages"][-1].pretty_print()


