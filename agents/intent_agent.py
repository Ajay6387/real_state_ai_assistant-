# agents/intent_agent.py

import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew

class IntentAgent:
    def __init__(self):
        self.agent = Agent(
            role="Intent Detection Agent",
            goal="Understand if the user wants to buy or sell a home.",
            backstory=(
                "You are a real estate assistant skilled at determining whether a customer "
                "wants to buy or sell a house. You must return only 'BUY' or 'SELL'."
            ),
            verbose=True,
            llm="groq/llama3-70b-8192"# ✅ Correct usage for Groq + Mixtral
        )

    def run(self, user_input):
        cleaned_input = user_input.strip().upper()
        if cleaned_input in ["BUY", "SELL"]:
            return cleaned_input, f"User explicitly said '{cleaned_input}'"

        task = Task(
            description=f"Determine the user's intent from this message: '{user_input}'. Reply ONLY with 'BUY' or 'SELL'.",
            expected_output="Return either 'BUY' or 'SELL' only.",
            agent=self.agent
        )

        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            verbose=False  # Turn off console spam
        )

        # Capture the reasoning manually
        result = crew.kickoff()
        reasoning_log = str(result)

        if hasattr(result, "final_output"):
            return result.final_output.strip().upper(), reasoning_log
        else:
            return str(result).strip().upper(), reasoning_log
