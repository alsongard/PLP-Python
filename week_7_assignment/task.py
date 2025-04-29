"""
Task 1: Load and Explore the Dataset
Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
Load the dataset using pandas.
Display the first few rows of the dataset using .head() to inspect the data.
Explore the structure of the dataset by checking the data types and any missing values.
Clean the dataset by either filling or dropping any missing values.
Task 2: Basic Data Analysis
Compute the basic statistics of the numerical columns (e.g., mean, median, standard deviation) using .describe().
Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
Identify any patterns or interesting findings from your analysis.
Task 3: Data Visualization
Create at least four different types of visualizations:
Line chart showing trends over time (for example, a time-series of sales data).
Bar chart showing the comparison of a numerical value across categories (e.g., average petal length per species).
Histogram of a numerical column to understand its distribution.
Scatter plot to visualize the relationship between two numerical columns (e.g., sepal length vs. petal length).
Customize your plots with titles, labels for axes, and legends where necessary.
"""


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_df = pd.read_csv("./data/traffic_accidents.csv")


# DATA PREPROCESSING
print(data_df.shape)
print(data_df.head())



print(data_df.isna().sum()) # no null vaues

print(data_df.info())


data_df['accident_time'] = data_df['crash_date'].str.extract(r"(..:..:..)")
print(data_df)

data_df['time_for_day'] = data_df['crash_date'].str.extract(r"([A-Z]+)")
print(data_df)

data_df['accident_date'] = data_df['crash_date'].str.extract(r"(../../....)")
print(data_df)
print(data_df.info())

data_df.to_csv('./data/cleaned_traffic_data.csv', index=False)
print(data_df.isna().sum()) # no null values

new_data_df = pd.read_csv("./data/cleaned_traffic_data.csv")

print(new_data_df)
print(new_data_df.info())

new_data_df = new_data_df.drop('crash_date', axis=1)
print(new_data_df.info())


# group data
"""
what can we analyze from the accidents data
1. which day, time, has more accidents
2. find the correlation between the different features
3. 
"""


# question 1

print('Time for day value_counts')
print(new_data_df['time_for_day'].value_counts())

print('\nweather_condition value_counts')
print(new_data_df['weather_condition'].value_counts())

print('\ntrafficway_type value_counts')
print(new_data_df["trafficway_type"].value_counts())

print('\nalignment value_counts')
print(new_data_df["alignment"].value_counts())

print('\nroadway_surface_cond value_counts')
print(new_data_df["roadway_surface_cond"].value_counts())

print('\nroad_defect value_counts')
print(new_data_df["road_defect"].value_counts())

print('\nintersection_related_i')
print(new_data_df["intersection_related_i"].value_counts())

print('\nprim_contributory_cause')
print(new_data_df["prim_contributory_cause"].value_counts())

print('\ncrash_day_of_week value_counts')
print(new_data_df["crash_day_of_week"].value_counts())


"""
results:
time_for_day
PM    136823
AM     72483
"""


# plot the barChart
sns.countplot(data=new_data_df, x=new_data_df['time_for_day'], hue='time_for_day')
plt.savefig('time_for_day_barchart.png')
plt.title('Accident Distribution on Day time')
plt.legend(new_data_df['time_for_day'])
plt.show()


# check the correlation between differnt featues
# to perform correlation we will need to drop some columns 
# perform feature engineering = label encoding, one hot encoding
# this depends on norminal or ordinal data

# dropping unneccesary columns
new_data_df.drop('crash_date', axis=1, inplace=True)
time_for_day_dict = {"AM": 0, "PM": 1}
new_data_df['time_for_day'] = new_data_df['time_for_day'].map(time_for_day_dict)
print(new_data_df['time_for_day'])
new_data_df_corr = new_data_df.corr()
print(new_data_df_corr)

print(new_data_df['lighting_condition'].value_counts()) # crash_type	The overall type of the crash.

print(new_data_df['injuries_fatal'].value_counts())
print(new_data_df['injuries_incapacitating'].value_counts())
print(new_data_df['most_severe_injury'].value_counts())

new_data_df['accident_date'] = pd.to_datetime(new_data_df['accident_date'])
print(new_data_df.info())
# create new month column
new_data_df['month'] =  new_data_df['accident_date'].dt.month
print(new_data_df['month'])

# groupby month
traffic_month_df = new_data_df.groupby('month')
print(traffic_month_df.first())
monthly_data = traffic_month_df['month'].sum()
print(monthly_data)
print(type(monthly_data))

monthly_df = monthly_data.to_frame()
print(monthly_df)

# reset indx to convert month into a column
monthly_df = monthly_data.reset_index(name='total')
print(monthly_df)



sns.barplot(data=monthly_df, x='month', y='total', hue='month')
plt.title('Traffic Count based Month')
plt.savefig('traffic_count_based_month')
plt.show()

print(new_data_df['accident_date'].dt.year.min())
print(new_data_df['accident_date'].dt.year.max())

