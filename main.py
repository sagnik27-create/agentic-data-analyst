from app.agent.agent import Agent

if __name__ == "__main__":
    print("Starting agent...")

    agent = Agent(goal="Analyze CSV and give insights")
    agent.run()

    print("Agent finished.")
