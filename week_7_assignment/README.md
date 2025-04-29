# traffic data analysis

## Description
The dataset used shows traffic accidents from the year 2013 to 2025. The features of the dataset are provided below. 

## Installation:
1. **Setup your environment**
```
python3 -m venv . 
source bin/activate
pip install -r requirements.txt
```

2. **Usage**
To view the different charts run:
```
streamlit run traffic_streamlit_view.py
```
To view the analysis done:  
**Before running ensure to go through the file**
```
python3 task.py
```

**Challenges**
1. lack of domain knowledge on traffic data set
2. lack of severiry column
3. lack of expertise skills


## features of the data
Columns:
| ColumnName | Description | 
| --- | --- |
| crash_date | The date the accident occurred.|
| traffic_control_device | The type of traffic control device involved (e.g., traffic light, sign).|
| weather_condition | The weather conditions at the time of the accident.|
| lighting_condition | The lighting conditions at the time of the accident.|
| first_crash_type | The initial type of the crash (e.g., head-on, rear-end).|
| trafficway_type | The type of roadway involved in the accident (e.g., highway, local road).|
| alignment | The alignment of the road where the accident occurred (e.g., straight, curved).|
| roadway_surface_cond | The condition of the roadway surface (e.g., dry, wet, icy).|
| road_defect | Any defects present on the road surface.|
| crash_type | The overall type of the crash.|
| intersection_related_i | Whether the accident was related to an intersection.|
| damage | The extent of the damage caused by the accident.|
| prim_contributory_cause | The primary cause contributing to the crash.|
| num_units | The number of vehicles involved in the accident.|
| most_severe_injury | The most severe injury sustained in the crash.|
| injuries_total | The total number of injuries reported.|
| injuries_fatal | The number of fatal injuries resulting from the accident.|
| injuries_incapacitating | The number of incapacitating injuries. |
| injuries_non_incapacitating | The number of non-incapacitating injuries. |
| injuries_reported_not_evident | The number of injuries reported but not visibly evident. |
| injuries_no_indication | The number of cases with no indication of injury. |
| crash_hour | The hour the accident occurred. |
| crash_day_of_week | The day of the week the accident occurred. |
| crash_month | The month the accident occurred. |
