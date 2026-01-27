from app.agent.llm import get_llm

llm = get_llm()

def reflect(code: str, error: str):
    prompt = f"""
The following Python code failed:

{code}

Error:
{error}

Fix the code.
Return ONLY corrected Python code.
"""
    return llm.invoke(prompt).content

