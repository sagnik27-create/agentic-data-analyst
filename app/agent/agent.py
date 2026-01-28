from app.agent.state import AgentState
from app.agent.planner import Planner
from app.agent.executor import ToolExecutor
from app.agent.reflector import Reflector


class Agent:
    def __init__(self, goal: str):
        self.state = AgentState(goal)
        self.planner = Planner()
        self.executor = ToolExecutor()
        self.reflector = Reflector()   # ✅ missing before

    def run(self):
        self.state.plan = self.planner.create_plan(self.state.goal)

        while not self.state.done and not self.state.failed:
            try:
                action = self.state.plan[self.state.current_step_index]
                result = self.executor.execute(action, self.state)

                self.state.memory.append({
                    "action": action,
                    "result": result
                })

                # reset retry state on success
                self.state.retry_count = 0
                self.state.current_step_index += 1

                if self.state.current_step_index >= len(self.state.plan):
                    self.state.done = True

            except Exception as e:
                self.state.retry_count += 1
                print("Error:", e)

                if self.state.retry_count >= self.state.max_retries:
                    # 🔁 REFLECT + REPLAN
                    new_plan = self.reflector.reflect(e, self.state)

                    if new_plan:
                        print("Re-planning based on reflection")
                        self.state.plan = new_plan
                        self.state.current_step_index = 0
                        self.state.retry_count = 0
                    else:
                        print("Reflection failed. Aborting agent.")
                        self.state.failed = True
