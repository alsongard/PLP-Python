import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt
import plotly.express as px
"# TRAFFIC DATA ANALYSIS"

data_df = pd.read_csv("./data/traffic_accidents.csv")

data_df

st.text(f'Rows of the dataset is : {data_df.shape[0]}')
st.text(f'Columns of the dataset is : {data_df.shape[1]}')



st.write("data features/columns")
"""
Data columns (total 24 columns):
| Index | Column  |  Dtype |
| --- | --- | --- |
|0 |   crash_date |                     object | 
|1 |   traffic_control_device |         object | 
|2 |   weather_condition |              object | 
|3 |   lighting_condition |             object | 
|4 |   first_crash_type |               object | 
|5 |   trafficway_type |                object | 
|6 |   alignment |                      object | 
|7 |   roadway_surface_cond |           object | 
|8 |   road_defect |                    object | 
|9 |   crash_type |                     object | 
|10 |  intersection_related_i |         object | 
|11 |  damage |                         object | 
|12 |  prim_contributory_cause |        object | 
|13 |  num_units |                      int64 |  
|14 |  most_severe_injury |             object | 
|15 |  injuries_total |                 float64 |
|16 |  injuries_fatal |                 float64 |
|17 |  injuries_incapacitating |        float64 |
|18 |  injuries_non_incapacitating |    float64 |
|19 |  injuries_reported_not_evident |  float64 |
|20 |  injuries_no_indication |         float64 |
|21 |  crash_hour |                     int64 |  
|22 |  crash_day_of_week |              int64 |  
|23 |  crash_month |                    int64 |

"""


data_df['accident_time'] = data_df['crash_date'].str.extract(r"(..:..:..)")

data_df['time_for_day'] = data_df['crash_date'].str.extract(r"([A-Z]+)")

data_df['accident_date'] = data_df['crash_date'].str.extract(r"(../../....)")

data_df



# question 1

"## VALUE COUNTS CHARTS FOR DATASET FEATURES"
print('Time for day value_counts')
time_for_day_value_counts = data_df['time_for_day'].value_counts()
time_for_day_value_counts = time_for_day_value_counts.reset_index()
time_for_day_value_counts.columns = ['dayTime', 'count']
# plot using piechart
# the following offfers virtualization of the value_counts though not appealing
# time_for_day_pie_chart = alt.Chart(time_for_day_value_counts).mark_arc().encode(
#     theta='count',
#     color='dayTime'
# )
# st.altair_chart(time_for_day_pie_chart, use_container_width=True)
# plt.pie(time_for_day_value_counts.counts, labels=time_for_day_value_counts['dayTime'])
# plt.show()
'### **Accident Chart based on Day time**'
fig = px.pie(
    data_frame=time_for_day_value_counts,
    names='dayTime',
    values='count'
)

st.plotly_chart(fig, use_container_width=False)
st.text(data_df['time_for_day'].value_counts())



'### **weather_condition value_counts**' 
# st.text(data_df['weather_condition'].value_counts())
weather_condition_value_counts = data_df['weather_condition'].value_counts()
weather_condition_value_counts = weather_condition_value_counts.reset_index()
weather_condition_value_counts.columns = ['Weather_Condition', 'counts']

fig = px.pie(
    data_frame=weather_condition_value_counts,
    names='Weather_Condition',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)

'### **trafficway_type value_counts**'
trafficway_type_value_counts  = data_df["trafficway_type"].value_counts()
trafficway_type_value_counts = trafficway_type_value_counts.reset_index()
trafficway_type_value_counts.columns = ['TrafficWay_Type', 'counts']


fig = px.pie(
    data_frame=trafficway_type_value_counts,
    values='counts',
    names='TrafficWay_Type'
)
st.plotly_chart(fig, use_container_width=True)
# st.text(data_df["trafficway_type"].value_counts())

'### **alignment value_counts**'
alignment_value_counts = data_df["alignment"].value_counts()
alignment_value_counts = alignment_value_counts.reset_index()
alignment_value_counts.columns = ['Alignment_category', 'counts']

fig = px.pie(
    data_frame=alignment_value_counts,
    names='Alignment_category',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)
# st.text(data_df["alignment"].value_counts())





'### **roadway_surface_cond value_counts**'
st.text(data_df["roadway_surface_cond"].value_counts())
roadway_surface_cond_value_count = data_df["roadway_surface_cond"].value_counts()
roadway_surface_cond_value_count = roadway_surface_cond_value_count.reset_index()
roadway_surface_cond_value_count.columns = ['roadway_condition', 'counts']

fig = px.pie(
    data_frame=roadway_surface_cond_value_count,
    names='roadway_condition',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)



'### **road_defect value_counts**'
road_defect_value_count = data_df["road_defect"].value_counts()
road_defect_value_count = road_defect_value_count.reset_index()
road_defect_value_count.columns = ['Road_defect', 'counts']
fig = px.pie(
    data_frame=road_defect_value_count,
    names='Road_defect',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)
# st.text(data_df["road_defect"].value_counts())




'### **intersection_related_i'
intersection_related_i_value_counts = data_df["intersection_related_i"].value_counts()
intersection_related_i_value_counts = intersection_related_i_value_counts.reset_index()
intersection_related_i_value_counts.columns = ['intersection_related_i', 'counts']
fig = px.pie(
    data_frame=intersection_related_i_value_counts,
    names='intersection_related_i',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)



'### **prim_contributory_cause**'
prim_contributory_cause_value_counts = data_df["prim_contributory_cause"].value_counts()
prim_contributory_cause_value_counts  = prim_contributory_cause_value_counts.reset_index()
prim_contributory_cause_value_counts.columns = ['prim_contributory_cause' , 'counts']

fig = px.pie(
    data_frame=prim_contributory_cause_value_counts,
    names='prim_contributory_cause',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)

'### **crash_day_of_week value_counts**'
crash_day_of_week_value_counts = data_df["crash_day_of_week"].value_counts()
crash_day_of_week_value_counts = crash_day_of_week_value_counts.reset_index()
crash_day_of_week_value_counts.columns = ['crash_day_of_week', 'counts']

fig = px.pie(
    data_frame=crash_day_of_week_value_counts,
    names='crash_day_of_week',
    values='counts'
)
st.plotly_chart(fig, use_container_width=True)