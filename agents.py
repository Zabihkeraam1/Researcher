from crewai import Agent, LLM
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
load_dotenv()


search_tool = SerperDevTool()
llm = LLM(
    model=os.getenv("MODEL_NAME"),
    api_key=os.getenv("HF_TOKEN")
)

researcher = Agent(
    role="Researcher",
    goal="Find accurate information",
    backstory="""
    You are an expert researcher that finds reliable information.
    """,
    llm=llm,
    tools=[search_tool], # WEB SEARCH TOOL
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Write easy-to-read responses",
    backstory="""
    You are a technical writer.
    """,
    llm=llm,
    verbose=True
)