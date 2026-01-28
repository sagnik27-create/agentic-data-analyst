class Planner:
    def create_plan(self, goal: str):
        print("Planning for goal:", goal)

        return [
            "load_data",
            "clean_data",
            "analyze_data",
            "summarize_results"
        ]
