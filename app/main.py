import pandas as pd
from app.agent.graph import build_agent

if __name__ == "__main__":
    print("Starting agent...")

    df = pd.read_csv("sample.csv")

    agent = build_agent()

    state = {
        "goal": "Find average calories and plot calories vs duration",
        "df": df
    }

    agent.invoke(state)

    print("Agent finished.")

