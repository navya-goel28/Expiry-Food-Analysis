import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=['Purchase_Date', 'Expiry_Date', 'Consumed_Date'])
    return df
