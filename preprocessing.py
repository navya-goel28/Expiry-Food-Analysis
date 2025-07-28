import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df['Days_To_Expire'] = (df['Expiry_Date'] - df['Purchase_Date']).dt.days
    df['Consumed'] = ~df['Consumed_Date'].isna()
    df['Wasted'] = df['Consumed_Date'].isna() | (df['Consumed_Date'] > df['Expiry_Date'])
    df['Days_Stored'] = (df['Consumed_Date'] - df['Purchase_Date']).dt.days.fillna(0)
    df['Month'] = df['Purchase_Date'].dt.month
    return df
