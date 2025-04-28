"""
Task Requirements:
Download or create a CSV file called sales_data.csv with the following columns:
Date (YYYY-MM-DD)
Product
Quantity Sold
Revenue ($)
Write a Python script to:
Load the CSV file using pandas.
Calculate the total revenue.
Find the best-selling product (based on Quantity Sold).
Identify the day with the highest sales.
Save the results to a new file called sales_summary.txt.
Print the insights in a user-friendly format.
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data_df = pd.read_csv("./data/sales.csv")
print(data_df)

# for item in data_df.columns:
#     print(item)


# DATA PREPROCESSING
# print(data_df.isna().sum()) # no null values

# print(data_df.info())



# get statistics

#  get number of products being sold
print(data_df["Product Type"].value_counts())

print(len(data_df["Product Type"]))

print(data_df["Product Type"].isna())
sns.countplot(y=data_df["Product Type"], data=data_df, hue='Product Type')
plt.title('Product Type Sales')
# plt.savefig('product_type_value_counts_bar_chart.png')

# plt.show()

# plotting using pie chart
product_value_counts = data_df["Product Type"].value_counts()
print(product_value_counts.index) # list
print(product_value_counts.values) # list


fig, ax = plt.subplots(figsize=(8,10))
ax.pie(
    product_value_counts.values,
    labels=product_value_counts.index,
    autopct="%1.1f%%"
)
ax.axis('equal')
ax.set_title('Product Type Purchase Sales')
plt.legend(product_value_counts.index, loc='upper right')
# plt.savefig('product_type_value_counts_pie_chart.png')
# plt.show()


# highest selling product
sales_sum = data_df['Sales'].sum()
print(f'The total value of sales is : {sales_sum}') 


# get highest sales
max_sales_row = data_df[data_df['Sales'] == data_df['Sales'].max()]
print(max_sales_row) # 2 max rows

# print(max_sales_row['Product Type'].unique())

highest_selling_product = max_sales_row['Product Type'].unique()
print(f'Item in highest_selling_product is {highest_selling_product}')

try:
    with open('sales_summary.txt', 'w') as file:
        highest_selling_product_row = max_sales_row.to_string()
        file.write(f"the higest selling product is : {highest_selling_product} \n" 
                   f"The data for the highest selling product is:\n {highest_selling_product_row}"
        ) 
except Exception as e:
    print(f"ERROR : {e}")
