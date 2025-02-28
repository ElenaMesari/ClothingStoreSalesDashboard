import streamlit as st
import pandas as pd
import sqlite3
import altair as alt

 
st.set_page_config(page_title="Clothing Store Sales Dashboard", page_icon="👗")
st.title("👗 Clothing Store Sales, Price, and Inventory Dashboard")
 


@st.cache_data
def load_data():
    conn = sqlite3.connect('clothing_sales.db')
    query = """
    SELECT year, category, product_name, sales, price, inventory, (sales * price) AS total_sales_value
    FROM sales
    WHERE category IN ('T-shirts', 'Jeans', 'Jackets')
    AND year BETWEEN 2020 AND 2022
    ORDER BY year DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

 
categories = st.multiselect(
    "Select Categories",
    df['category'].unique(),
    ['T-shirts', 'Jeans', 'Jackets']
)

 
years = st.slider("Select Year Range", 2020, 2022, (2020, 2022))

df_filtered = df[
    (df['category'].isin(categories)) & 
    (df['year'].between(years[0], years[1]))
]

st.dataframe(df_filtered)

 
chart = alt.Chart(df_filtered).mark_bar().encode(
    x=alt.X('year:N', title='Year'),
    y=alt.Y('total_sales_value:Q', title='Total Sales Value ($)'),
    color='category:N',
    column='category:N'
).properties(title="Clothing Sales by Category and Year", height=300)

 
st.altair_chart(chart, use_container_width=True)
