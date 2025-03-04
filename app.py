import os
import streamlit as st
from crewai import Agent, Task, Crew
import litellm
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"] = "your_api_key"  

litellm.api_key = os.environ["GROQ_API_KEY"]
litellm.model = "groq/llama3-8b-8192"

planner = Agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You are an expert content strategist specializing in blog outline creation.",
    allow_delegation=False,
    verbose=True,
    memory=True,
    max_iter=3,
    model="groq/llama3-8b-8192" 
)

st.title("AI Content Planner with CrewAI (Groq-3)")

topic = st.text_input("Enter the blog topic:")

if st.button("Generate Blog Outline"):
    if topic:
        # Define a task for the agent
        task = Task(
            name="Generate Blog Outline",
            description="Create a structured blog outline for the given topic.",
            expected_output="A well-organized blog outline covering key points and subtopics.",
            instructions=f"Generate a detailed blog outline on the topic: {topic}.",
            agent=planner
        )

        crew = Crew(agents=[planner], tasks=[task])

        result = crew.kickoff()

        st.subheader("Generated Blog Outline:")
        st.write(result)
    else:
        st.error("Please enter a blog topic.")
