from langgraph.graph import StateGraph, END
from app.agent.planner import plan
from app.agent.reflector import reflect
from app.tools.python_tool import run_python

MAX_STEPS = 3

def build_agent():
    graph = StateGraph(dict)

    def planner_node(state):
        step = state.get("step", 0) + 1
        print(f"\n[Planner] Step {step}")

        if step > MAX_STEPS:
            print("[Agent] Max steps reached. Stopping.")
            return {"done": True}

        code = plan(
            state["goal"],
            columns=list(state["df"].columns)
        )

        print("[Planner Code]\n", code)

        return {
            "code": code,
            "df": state["df"],
            "goal": state["goal"],
            "step": step
        }

    def executor_node(state):
        print("[Executor] Running code...")
        result = run_python(state["code"], state["df"])

        if not result["success"]:
            print("[Executor Error]", result["error"])
        else:
            print("[Executor] Success")

        return {
            "result": result,
            "code": state["code"],
            "df": state["df"],
            "goal": state["goal"],
            "step": state["step"]
        }

    def reflector_node(state):
        if state.get("done"):
            return state

        if not state["result"]["success"]:
            print("[Reflector] Fixing code...")

            # hard stop if syntax keeps failing
            if "invalid syntax" in state["result"]["error"].lower():
                print("[Agent] Syntax error persists. Stopping.")
                return {"done": True}

            fixed_code = reflect(
                state["code"],
                state["result"]["error"]
            )

            return {
                "code": fixed_code,
                "df": state["df"],
                "goal": state["goal"],
                "step": state["step"]
            }

        print("[Agent] Task completed successfully.")
        return {"done": True}

    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_node)
    graph.add_node("reflector", reflector_node)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "reflector")
    graph.add_conditional_edges(
        "reflector",
        lambda state: END if state.get("done") else "executor"
    )

    return graph.compile()

