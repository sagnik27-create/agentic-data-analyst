import pandas as pd


def load_csv(path: str):
    print(f"Loading CSV from {path}")
    return pd.read_csv(path)


def clean_dataframe(df):
    print("Cleaning dataframe (dropping NA)")
    return df.dropna()


def analyze_dataframe(df):
    print("Analyzing dataframe")
    return {
        "average_calories": df["Calories"].mean()
    }
