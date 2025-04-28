import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px


data_df = pd.read_csv("./data/sales.csv")

import seaborn as sns

"# SALES DATA ANALYSIS"
st.text(f'The rows for the dataset is : {data_df.shape[0]}')
st.text(f'The columns for the dataset is : {data_df.shape[1]}')

st.write(data_df)



# columns
st.write("Description for each column and there datatype")

"""
| columnName | Description | datatype | 
| --- | --- | --- |
| Area Code | Store's Code | int64|
| State | Store's State | object|
| Market | Store's Region | object|
| Market Size | Store's Size | object|
| Profit | Profits in Dollars ($) | float64|
| Margin | Profit + Total Expenses ($) OR Sales - COGS ($) | float64|
| Sales | Values Acquired in Sales ($) | float64|
| COGS | Cost of Goods Sold ($) | float64|
| Total Expenses | Total Expenses to get the Product to Sell ($) | float64|
| Marketing | Expenses in Marketing ($) | float64|
| Inventory | Inventory Value of the Product in the Sale Moment ($) | float64|
| Budget Profit | Expected Profit ($) | float64|
| Budget COGS | Expected COGS ($) | float64|
| Budget Margin | Expected Profit + Expected Total Expenses ($) OR Expected Sales - Expected COGS ($) | float64|
| Budget Sales | Expected Value Acquired in Sales ($) | float64|
| ProductID | Product ID | int64|
| Date | Sale Date | object|
| Product Type | Product Category | object|
| Product | Product Description | object|
| Type | Type | object| 

"""

max_sales_row = data_df[data_df['Sales'] == data_df['Sales'].max()]
st.text(f"Highest Sales in A day : {data_df['Sales'].max()}")
max_sales_row


max_sales_row['Product Type']


# ploting bar chart

# when using  value_counts() method it returns a series object.
# however the st.bar_chart() function expects a dataframe
# hence the use of reset_index() function which converts the series object into a dataframe
# 
# after this you set the columns
# dataframe.columns = ['columnName', ]


product_value_counts = data_df['Product Type'].value_counts().reset_index()
# product_value_counts.columns
product_value_counts.columns = ['category', 'count']

# this code provides a bar chart though no solution for different colors  for bar
# st.bar_chart(data=product_value_counts, x='category', x_label='category', y_label='count')

chart =alt.Chart(product_value_counts).mark_bar(size=50).encode(
    x='category',
    y='count',
    color='category:N'
    # color=alt.value('green') changes color to green
)
st.altair_chart(chart, use_container_width=True)


# plotting value counts using pie chart
# the following chart is displays the chart however with no percentage: %1.1f%%
st.subheader('Product Purchase Distribution')
pieChart = alt.Chart(product_value_counts).mark_arc().encode(
    theta='count',
    color='category'
)
st.altair_chart(pieChart, use_container_width=True)

st.subheader('Product Purchase Distribution')
fig  = px.pie(
    data_frame=product_value_counts,
    names='category',
    values='count'
)
st.plotly_chart(fig, use_container_width=True)