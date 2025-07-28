import pandas as pd

def category_waste_stats(df):
    return df.groupby("Category")["Wasted"].mean().reset_index().rename(columns={"Wasted": "Waste_Rate"})

def monthly_waste_trend(df):
    df['Month'] = df['Purchase_Date'].dt.month
    return (
        df.groupby("Month")["Wasted"]
        .mean()
        .reset_index()
        .rename(columns={"Wasted": "Waste_Rate"})
    )

def expiry_vs_consumption_delay(df: pd.DataFrame):
    return df[['Days_To_Expire', 'Days_Stored']]