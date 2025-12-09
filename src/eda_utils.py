import pandas as pd

def calculate_loss_ratio(df: pd.DataFrame) -> pd.DataFrame:
    df["LossRatio"] = df["ClaimAmount"] / df["Premium"]
    return df

def summarize_numeric(df: pd.DataFrame):
    return df.describe().T
