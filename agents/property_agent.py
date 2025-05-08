from crewai import Agent, Task, Crew

class PropertyAgent:
    def __init__(self):
        self.agent = Agent(
            role="Property Recommendation Agent",
            goal="Suggest suitable properties based on user's intent, location, and budget.",
            backstory=(
                "You are a helpful real estate assistant that recommends properties for buying or selling "
                "based on user needs, budget, and location. Your suggestions should be practical and concise."
            ),
            llm="groq/llama3-8b-8192",  # ✅ Updated to supported Groq model
            verbose=True
        )

    def run(self, intent, location, budget):
        query = (
            f"The user wants to {intent.lower()} a house in {location} with a budget of {budget}. "
            f"Suggest 3 suitable property listings with descriptions and price."
        )

        task = Task(
            description=query,
            expected_output="Return 3 listings with title, price, and short description.",
            agent=self.agent
        )

        crew = Crew(
            agents=[self.agent],
            tasks=[task],
            verbose=True
        )

        result = crew.kickoff()
        return result.strip()
