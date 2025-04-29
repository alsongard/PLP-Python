import pandas as pd
data = {
    'purchase_date': ['2024-01-15', '2024-01-20', '2024-02-14', '2024-02-25', '2024-03-05'],
    'amount': [120, 250, 175, 80, 200]
}


data_df = pd.DataFrame(data)
print(data_df)
print(data_df.info())


data_df['purchase_date'] = pd.to_datetime(data_df['purchase_date'])
print(data_df.info())


# grouping data
# extract month
data_df['month']  = data_df['purchase_date'].dt.month
print(data_df)

new_data_df = data_df.groupby('month')
print(new_data_df['amount'].sum())