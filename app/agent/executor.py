from app.tools.csv_tools import load_csv, clean_dataframe, analyze_dataframe


class ToolExecutor:
    def execute(self, action: str, state):
        print(f"Executing action: {action}")

        if action == "load_data":
            state.data = load_csv("sample.csv")
            return "data_loaded"

        elif action == "clean_data":
            state.data = clean_dataframe(state.data)
            return "data_cleaned"

        elif action == "analyze_data":
            state.analysis = analyze_dataframe(state.data)
            return state.analysis

        elif action == "summarize_results":
            return state.analysis

        else:
            raise ValueError(f"Unknown action: {action}")
