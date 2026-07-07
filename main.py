from crewai import Crew, Process
from agents import researcher, writer
from tasks import research_task, writing_task

crew = Crew(
    agents=[
        researcher,
        writer
    ],
    tasks=[
        research_task,
        writing_task
    ],
    process=Process.sequential,
    verbose=True
)
topic = input("Enter a topic: ")
result = crew.kickoff(
    inputs={
        "topic": topic
    }
)

print(result)