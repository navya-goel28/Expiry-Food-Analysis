import pandas as pd
import random
from datetime import datetime, timedelta

# ⏳ Simulate realistic items and shelf lives
items = [
    ('Milk', 'Dairy', 5), ('Bread', 'Bakery', 4), ('Eggs', 'Protein', 14),
    ('Apples', 'Fruit', 10), ('Spinach', 'Vegetable', 3), ('Yogurt', 'Dairy', 7),
    ('Bananas', 'Fruit', 5), ('Rice', 'Grains', 180), ('Chicken', 'Protein', 3),
    ('Cheese', 'Dairy', 20), ('Lettuce', 'Vegetable', 4), ('Fish', 'Protein', 2),
    ('Tomatoes', 'Vegetable', 5), ('Pasta', 'Grains', 365), ('Ice Cream', 'Frozen', 180),
    ('Soup', 'Canned', 730)
]

rows = []
for _ in range(500):  # 🔄 generate 500 rows
    item, category, shelf_life = random.choice(items)
    
    # Simulate different months (seasonal variation)
    base_date = datetime(2025, random.choice([5, 6, 7]), random.randint(1, 28))  # May–July
    purchase_date = base_date
    expiry_date = purchase_date + timedelta(days=shelf_life)

    # 80% chance it's consumed, 20% chance it's wasted
    consumed = random.choices([True, False], weights=[80, 20])[0]
    consumed_date = (
        purchase_date + timedelta(days=random.randint(1, shelf_life + 5))
        if consumed else pd.NaT
    )

    quantity = random.randint(1, 5)
    rows.append([
        item, category, purchase_date, expiry_date, consumed_date, quantity
    ])

df = pd.DataFrame(rows, columns=[
    'Item', 'Category', 'Purchase_Date', 'Expiry_Date', 'Consumed_Date', 'Quantity'
])

df.to_csv('data/synthetic_food_data.csv', index=False)
print(f"✅ Generated synthetic_food_data.csv with {len(df)} rows")
