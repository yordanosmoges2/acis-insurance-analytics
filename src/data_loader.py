import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    try:
        return pd.read_csv(
            filepath,
            sep="|",         # <-- VERY IMPORTANT
            header=0,
            encoding="utf-8",
            engine="python"  # <-- fixes tokenizing issues
        )
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()





