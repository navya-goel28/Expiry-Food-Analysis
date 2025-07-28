import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_waste(trend_series):
    plt.figure(figsize=(10, 5))
    trend_series.plot(kind='bar', color='tomato')
    plt.title("Monthly Average Waste Rate")
    plt.ylabel("Waste Rate")
    plt.xlabel("Month")
    plt.grid(True)
    plt.show()

def plot_category_waste(stats_series):
    stats_series.plot(kind='barh', color='salmon')
    plt.title("Waste Rate by Category")
    plt.xlabel("Waste Rate")
    plt.grid(True)
    plt.show()

def plot_expiry_vs_storage(df):
    sns.scatterplot(data=df, x='Days_To_Expire', y='Days_Stored', hue=(df['Days_Stored'] > df['Days_To_Expire']))
    plt.axline((0, 0), slope=1, color='gray', linestyle='--')
    plt.title("Days Stored vs Expiry Time")
    plt.xlabel("Days to Expiry")
    plt.ylabel("Days Stored")
    plt.show()