import traceback

def clean_code(code: str) -> str:
    # Remove markdown code fences if present
    if "```" in code:
        code = code.replace("```python", "")
        code = code.replace("```", "")
    return code.strip()

def run_python(code: str, df):
    code = clean_code(code)
    local_env = {"df": df}

    try:
        exec(code, {}, local_env)
        return {
            "success": True,
            "locals": local_env
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "traceback": traceback.format_exc()
        }
