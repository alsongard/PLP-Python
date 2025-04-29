import pandas as pd
data_df = pd.read_csv("./data/nba.csv")

print(data_df)

print(data_df.isna().sum())


data_df = data_df.dropna(axis=0)
print(data_df.isna().sum())
print(data_df)

team_df = data_df.groupby('Team')
print(team_df.first())