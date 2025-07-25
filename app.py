import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# 🔧 Import your custom functions
from src.preprocessing import add_features
from src.analysis import category_waste_stats, monthly_waste_trend, expiry_vs_consumption_delay

st.set_page_config(page_title="Food Expiry Pattern Dashboard", layout="wide")
st.title("🥚 Food Expiry Pattern Analysis")

# ------------------------------
# 🔀 Mode Selection
# ------------------------------
option = st.radio("Choose Data Input Mode:", [
    "📄 Upload CSV (synthetic data)",
    "📑 Manually Enter Items"
])

# ------------------------------
# 📄 CSV Upload Mode
# ------------------------------
if option == "📄 Upload CSV (synthetic data)":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"], key="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file, parse_dates=['Purchase_Date', 'Expiry_Date', 'Consumed_Date'])
        df = add_features(df)

        st.success(f"Loaded {len(df)} rows from uploaded file.")
        st.dataframe(df)

        st.subheader("🍽️ Waste Rate by Category")
        cat_stats = category_waste_stats(df)
        fig1, ax1 = plt.subplots()
        sns.barplot(x='Waste_Rate', y='Category', data=cat_stats, color='salmon', ax=ax1)
        st.pyplot(fig1)

        st.subheader("🗓️ Monthly Waste Trend")
        month_stats = monthly_waste_trend(df)
        fig2, ax2 = plt.subplots()
        sns.barplot(x='Month', y='Waste_Rate', data=month_stats, color='coral', ax=ax2)
        st.pyplot(fig2)

        st.subheader("⏳ Days Stored vs Days to Expiry")
        fig3, ax3 = plt.subplots()
        sns.scatterplot(data=df, x='Days_To_Expire', y='Days_Stored', hue='Wasted', ax=ax3)
        ax3.plot([0, df['Days_To_Expire'].max()], [0, df['Days_To_Expire'].max()], '--', color='gray')
        st.pyplot(fig3)

# ------------------------------
# 📑 Manual Entry Mode
# ------------------------------
elif option == "📑 Manually Enter Items":
    st.subheader("📑 Manually Enter Food Items")

    if "manual_items" not in st.session_state:
        st.session_state.manual_items = []

    with st.form("manual_entry_form", clear_on_submit=True):
        item = st.text_input("Item Name")
        category = st.selectbox("Category", ["Dairy", "Bakery", "Fruit", "Vegetable", "Protein", "Grains", "Other"])
        quantity = st.number_input("Quantity", min_value=1, max_value=100, value=1)
        shelf_life = st.number_input("Shelf Life (days)", min_value=1, max_value=365, value=7)
        consumed = st.checkbox("Was it consumed?")
        days_stored = st.slider("Days stored before consumption (if consumed)", 1, shelf_life+5) if consumed else None

        submitted = st.form_submit_button("Add Item")

        if submitted:
            purchase_date = pd.Timestamp.now().normalize()
            expiry_date = purchase_date + pd.Timedelta(days=shelf_life)
            consumed_date = purchase_date + pd.Timedelta(days=days_stored) if consumed else pd.NaT

            st.session_state.manual_items.append({
                "Item": item,
                "Category": category,
                "Quantity": quantity,
                "Purchase_Date": purchase_date,
                "Expiry_Date": expiry_date,
                "Consumed_Date": consumed_date
            })
            st.success(f"Added {item} to the list.")

    if st.session_state.manual_items:
        df_manual = pd.DataFrame(st.session_state.manual_items)
        st.write("Entered Items")
        st.dataframe(df_manual)

        df_manual = add_features(df_manual)

        st.subheader("🍽️ Waste Rate by Category (Manual Data)")
        cat_stats = category_waste_stats(df_manual)
        fig1, ax1 = plt.subplots()
        sns.barplot(x='Waste_Rate', y='Category', data=cat_stats, color='salmon', ax=ax1)
        st.pyplot(fig1)

        st.subheader("🗓️ Monthly Waste Trend (Manual Data)")
        month_stats = monthly_waste_trend(df_manual)
        fig2, ax2 = plt.subplots()
        sns.barplot(x='Month', y='Waste_Rate', data=month_stats, color='coral', ax=ax2)
        st.pyplot(fig2)

        st.subheader("⏳ Days Stored vs Days to Expiry")
        fig3, ax3 = plt.subplots()
        sns.scatterplot(data=df_manual, x='Days_To_Expire', y='Days_Stored', hue='Wasted', ax=ax3)
        ax3.plot([0, df_manual['Days_To_Expire'].max()], [0, df_manual['Days_To_Expire'].max()], '--', color='gray')
        st.pyplot(fig3)

        st.download_button("📂 Download Manual Data as CSV", df_manual.to_csv(index=False), "manual_data.csv")
