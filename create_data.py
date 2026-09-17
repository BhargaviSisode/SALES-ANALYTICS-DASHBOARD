import pandas as pd
import random
from datetime import datetime, timedelta

# Sample data generation
products = ['Laptop', 'Mobile', 'Headphones', 'Keyboard', 'Mouse', 'Monitor', 'Tablet']
categories = {'Laptop': 'Electronics', 'Mobile': 'Electronics', 'Headphones': 'Accessories',
              'Keyboard': 'Accessories', 'Mouse': 'Accessories', 'Monitor': 'Electronics', 'Tablet': 'Electronics'}
regions = ['North', 'South', 'East', 'West']

data = []
start_date = datetime(2024, 1, 1)

for i in range(200):
    product = random.choice(products)
    category = categories[product]
    region = random.choice(regions)
    price = random.randint(500, 50000)
    quantity = random.randint(1, 10)
    date = start_date + timedelta(days=random.randint(0, 300))
    
    data.append({
        'OrderID': i + 1,
        'Date': date.strftime('%Y-%m-%d'),
        'Product': product,
        'Category': category,
        'Region': region,
        'Price': price,
        'Quantity': quantity,
        'Total_Sales': price * quantity
    })

df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("Sample data created successfully!")
print(df.head())