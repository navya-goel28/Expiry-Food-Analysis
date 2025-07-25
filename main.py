# %%
import pandas as pd
from src.data_loader import load_data
from src.preprocessing import add_features
from src.analysis import category_waste_stats, monthly_waste_trend, expiry_vs_consumption_delay
from src.visualization import plot_monthly_waste, plot_category_waste, plot_expiry_vs_storage

def main():
    df = load_data('data/synthetic_food_data.csv')
    df = add_features(df)

    pd.set_option('display.max_columns', None) 
    print("✅ Data preview after feature engineering:")
    print(df.head()) 

    cat_stats = category_waste_stats(df)
    month_trend = monthly_waste_trend(df)
    expiry_vs_cons = expiry_vs_consumption_delay(df)


    print("📊 Waste Rate by Category:\n", cat_stats.to_string())
    print("\n📈 Monthly Waste Trend:\n", month_trend.to_string())

    plot_category_waste(cat_stats)
    plot_monthly_waste(month_trend)
    plot_expiry_vs_storage(expiry_vs_cons)

if __name__ == "__main__":
    main()
# %%
