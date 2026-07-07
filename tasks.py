from crewai import Task
from agents import researcher, writer

research_task = Task(
    description="""
    Research the following topic:

    {topic}

    Requirements:
    - Use the search tool to gather information.
    - Use reliable sources.
    - Return a concise summary in bullet points.
    - Include important facts only.
    """,
    expected_output="A concise research summary with bullet points.",
    agent=researcher
)

writing_task = Task(
    description="""
    Using ONLY the research provided by the previous task:

    - Write a beginner-friendly explanation.
    - Do not search the web.
    - Do not invent new facts.
    - Organize the explanation with headings.
    - End with a short conclusion.
    """,
    expected_output="A well-structured explanation in Markdown.",
    agent=writer
)