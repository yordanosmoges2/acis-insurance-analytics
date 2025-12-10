import pandas as pd
import numpy as np

def calculate_loss_ratio(df):
    # Ensure numeric types
    df["TotalClaims"] = pd.to_numeric(df["TotalClaims"], errors="coerce")
    df["TotalPremium"] = pd.to_numeric(df["TotalPremium"], errors="coerce")

    # Avoid division by zero
    df.loc[df["TotalPremium"] <= 0, "TotalPremium"] = np.nan

    # Loss Ratio = Claims / Premium
    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"]

    return df

