<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

# ---------- LOAD DATA ----------
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("===== BASIC DATA OVERVIEW =====")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nColumn Info:")
print(df.info())

# ---------- DATA CLEANING ----------
print("\n===== CHECKING FOR MISSING VALUES =====")
print(df.isnull().sum())

# Drop duplicates if any
df = df.drop_duplicates()

# ---------- ANALYSIS 1: Total Revenue ----------
total_revenue = df['Total_Sales'].sum()
print(f"\n===== TOTAL REVENUE: ₹{total_revenue:,.2f} =====")

# ---------- ANALYSIS 2: Revenue by Category ----------
category_revenue = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
print("\n===== REVENUE BY CATEGORY =====")
print(category_revenue)

# ---------- ANALYSIS 3: Revenue by Region ----------
region_revenue = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("\n===== REVENUE BY REGION =====")
print(region_revenue)

# ---------- ANALYSIS 4: Top 5 Best-Selling Products ----------
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\n===== TOP 5 BEST-SELLING PRODUCTS (by Quantity) =====")
print(top_products)

# ---------- ANALYSIS 5: Monthly Sales Trend ----------
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales)

# ---------- VISUALIZATION 1: Revenue by Category (Bar Chart) ----------
plt.figure(figsize=(8, 5))
category_revenue.plot(kind='bar', color='skyblue')
plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('revenue_by_category.png')
plt.show()

# ---------- VISUALIZATION 2: Monthly Sales Trend (Line Chart) ----------
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales (₹)')
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.show()

# ---------- VISUALIZATION 3: Region-wise Revenue (Pie Chart) ----------
plt.figure(figsize=(7, 7))
region_revenue.plot(kind='pie', autopct='%1.1f%%')
plt.title('Revenue Distribution by Region')
plt.ylabel('')
plt.tight_layout()
plt.savefig('region_revenue_pie.png')
plt.show()

=======
import pandas as pd
import matplotlib.pyplot as plt

# ---------- LOAD DATA ----------
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

print("===== BASIC DATA OVERVIEW =====")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nColumn Info:")
print(df.info())

# ---------- DATA CLEANING ----------
print("\n===== CHECKING FOR MISSING VALUES =====")
print(df.isnull().sum())

# Drop duplicates if any
df = df.drop_duplicates()

# ---------- ANALYSIS 1: Total Revenue ----------
total_revenue = df['Total_Sales'].sum()
print(f"\n===== TOTAL REVENUE: ₹{total_revenue:,.2f} =====")

# ---------- ANALYSIS 2: Revenue by Category ----------
category_revenue = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
print("\n===== REVENUE BY CATEGORY =====")
print(category_revenue)

# ---------- ANALYSIS 3: Revenue by Region ----------
region_revenue = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("\n===== REVENUE BY REGION =====")
print(region_revenue)

# ---------- ANALYSIS 4: Top 5 Best-Selling Products ----------
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
print("\n===== TOP 5 BEST-SELLING PRODUCTS (by Quantity) =====")
print(top_products)

# ---------- ANALYSIS 5: Monthly Sales Trend ----------
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
print("\n===== MONTHLY SALES TREND =====")
print(monthly_sales)

# ---------- VISUALIZATION 1: Revenue by Category (Bar Chart) ----------
plt.figure(figsize=(8, 5))
category_revenue.plot(kind='bar', color='skyblue')
plt.title('Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()
plt.savefig('revenue_by_category.png')
plt.show()

# ---------- VISUALIZATION 2: Monthly Sales Trend (Line Chart) ----------
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales (₹)')
plt.tight_layout()
plt.savefig('monthly_sales_trend.png')
plt.show()

# ---------- VISUALIZATION 3: Region-wise Revenue (Pie Chart) ----------
plt.figure(figsize=(7, 7))
region_revenue.plot(kind='pie', autopct='%1.1f%%')
plt.title('Revenue Distribution by Region')
plt.ylabel('')
plt.tight_layout()
plt.savefig('region_revenue_pie.png')
plt.show()

>>>>>>> 4878339c1bd4021fd5114562bf0aea45ceed8414
print("\n✅ Analysis complete! Charts saved as PNG files.")