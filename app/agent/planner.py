from langchain_core.prompts import ChatPromptTemplate
from app.agent.llm import get_llm

llm = get_llm()

planner_prompt = ChatPromptTemplate.from_template("""
You are an autonomous data analyst.

You are working with a pandas DataFrame named `df`.

IMPORTANT:
- df columns are exactly: {columns}
- Column names are case-sensitive
- You MUST use the exact column names

Task:
{goal}

Rules:
- Return ONLY valid executable Python code
- ALWAYS import required libraries (e.g. matplotlib.pyplot as plt)
- Do NOT include explanations
- Do NOT include markdown
- Do NOT include backticks
""")

def plan(goal: str, columns=None):
    messages = planner_prompt.format_messages(
        goal=goal,
        columns=columns
    )
    return llm.invoke(messages).content
