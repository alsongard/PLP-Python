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
import numpy as np
import seaborn as sns

data_df = pd.read_csv('./data/sales.csv')
print(data_df)



# data preprocessing
# print(data_df.isna().sum()) # no null things

# print(data_df.columns)
# print(data_df.info()) 
data_df['Date'] = data_df['Date'].replace('.00:00:00', "", regex=True)


# total revenue
total_revenue = data_df['Sales'].sum()
print(f'Total Sales are : {total_revenue}')

# Find the best-selling product (based on Quantity So
highest_selling_day_product = data_df[data_df['Sales'] == data_df['Sales'].max()]
print(highest_selling_day_product)


highest_selling_product = highest_selling_day_product['Product Type']
highest_product = highest_selling_day_product['Product Type']
print(type(highest_product))
highest_product = highest_product.unique()
highest_product = np.array2string(highest_product)
highest_product = highest_product.strip('[]')

print(f'The highest selling product is {highest_product}')


# Identify the day with the highest sales
# print(data_df['Date'])

print(highest_selling_day_product['Date'])


# visualization(EDA)
# provide visualization for the product Type
product_value_counts = data_df['Product Type'].value_counts() # returns index and counts series
print(product_value_counts)

# data_df['Product Type'].value_counts().plot(kind='bar')
# plt.show()

sns.countplot(data=data_df, y=data_df['Product Type'], orient='x', hue='Product Type')
plt.title('Product Type Distribution')
plt.legend(product_value_counts.index)
plt.savefig("./product_type_value_counts_bar_chart.png")
plt.show()


# pie chart
plt.figure(figsize=(8,8))
plt.pie(x=product_value_counts.values, labels=product_value_counts.index, autopct="%1.1f%%")
plt.title("Product Type Distribution")
plt.savefig("product_type_value_counts_pie_chart.png")
plt.show()

print(type(product_value_counts.index))
print(type(product_value_counts.values))




# save the results to a new file:
try:
    with open('sales_summary.txt', 'w') as file:
        max_row = highest_selling_day_product.to_string()
        file.write(
            f"Highest Selling Day is : \n{max_row}\n"
            f"Product with the highest sales is {highest_product}\n"
            f"The day with the most sales is : {highest_selling_day_product['Date']}"
        )
except Exception as e:
    print(f'Error ! : {e}')