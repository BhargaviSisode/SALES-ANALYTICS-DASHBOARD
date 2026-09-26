import streamlit as st
import pandas as pd
from google import genai
from config import GEMINI_API_KEY

# ---------- CONFIGURE GEMINI ----------
client = genai.Client(api_key=GEMINI_API_KEY)

st.title("📊 Sales Performance Analytics Dashboard")

# ---------- LOAD DATA ----------
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# ---------- SIDEBAR FILTER ----------
region_filter = st.sidebar.multiselect(
    "Select Region", 
    options=df['Region'].unique(), 
    default=df['Region'].unique()
)
filtered_df = df[df['Region'].isin(region_filter)]

# ---------- KPIs ----------
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{filtered_df['Total_Sales'].sum():,.0f}")
col2.metric("Total Orders", len(filtered_df))
col3.metric("Avg Order Value", f"₹{filtered_df['Total_Sales'].mean():,.0f}")

# ---------- CATEGORY REVENUE CHART ----------
st.subheader("Revenue by Category")
category_revenue = filtered_df.groupby('Category')['Total_Sales'].sum()
st.bar_chart(category_revenue)

# ---------- MONTHLY TREND ----------
st.subheader("Monthly Sales Trend")
filtered_df['Month'] = filtered_df['Date'].dt.to_period('M').astype(str)
monthly_sales = filtered_df.groupby('Month')['Total_Sales'].sum()
st.line_chart(monthly_sales)

# ---------- REGION REVENUE ----------
region_revenue = filtered_df.groupby('Region')['Total_Sales'].sum()

# ---------- TOP PRODUCTS ----------
top_products = filtered_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)

# ---------- RAW DATA TABLE ----------
st.subheader("Raw Data")
st.dataframe(filtered_df)


# =========================================
# 🤖 AI-POWERED INSIGHTS CHATBOT SECTION
# =========================================
st.divider()
st.subheader("🤖 Ask AI About Your Sales Data")

def create_data_summary():
    summary = f"""
    Sales Data Summary:
    - Total Revenue: ₹{filtered_df['Total_Sales'].sum():,.0f}
    - Total Orders: {len(filtered_df)}
    - Average Order Value: ₹{filtered_df['Total_Sales'].mean():,.0f}
    
    Revenue by Category:
    {category_revenue.to_string()}
    
    Revenue by Region:
    {region_revenue.to_string()}
    
    Monthly Sales Trend:
    {monthly_sales.to_string()}
    
    Top 5 Best-Selling Products (by Quantity):
    {top_products.to_string()}
    """
    return summary

user_question = st.text_input("Ask a question about your sales data (e.g., 'Which category should I focus on?')")

if st.button("Get AI Insight"):
    if user_question:
        with st.spinner("AI is analyzing your data..."):
            data_summary = create_data_summary()
            
            prompt = f"""
            You are a helpful sales data analyst. Based on the following sales data summary, 
            answer the user's question with clear, actionable business insights.
            
            {data_summary}
            
            User's Question: {user_question}
            
            Provide a concise, helpful answer (max 150 words).
            """
            
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            st.success("AI Insight:")
            st.write(response.text)
    else:
        st.warning("Please enter a question first!")