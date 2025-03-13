import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# Load the dataset
data = pd.read_csv('uber_trips_data.csv')

# Show the first few rows to understand the structure
data.head()
# Convert pickup_datetime and dropoff_datetime to datetime format
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])
data['dropoff_datetime'] = pd.to_datetime(data['dropoff_datetime'])

# Handle missing values (if any)
data = data.dropna()

# Create new columns for the analysis
data['trip_duration'] = (data['dropoff_datetime'] - data['pickup_datetime']).dt.total_seconds() / 60  # Duration in minutes
data['hour_of_day'] = data['pickup_datetime'].dt.hour
data['day_of_week'] = data['pickup_datetime'].dt.day_name()

# Display cleaned data
data.head()
plt.figure(figsize=(10,6))
sns.countplot(x='hour_of_day', data=data, palette='coolwarm')
plt.title('Trips Distribution by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Trips')
plt.show()
#Trips by day of the week
plt.figure(figsize=(10,6))
sns.countplot(x='day_of_week', data=data, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='coolwarm')
plt.title('Trips Distribution by Day of Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Trips')
plt.show()
#Average trip duration by hour
hourly_trip_duration = data.groupby('hour_of_day')['trip_duration'].mean()

plt.figure(figsize=(10,6))
hourly_trip_duration.plot(kind='line', marker='o', color='b')
plt.title('Average Trip Duration by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Trip Duration (minutes)')
plt.grid(True)
plt.show()
