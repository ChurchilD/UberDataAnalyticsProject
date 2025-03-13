import pandas as pd
import folium
from folium.plugins import HeatMap

# Generate a map centered around the average pickup location
data = pd.read_csv('uber_trips_data.csv')
map_center = [data['pickup_location_lat'].mean(), data['pickup_location_lon'].mean()]  # Adjust for actual latitude/longitude

uber_map = folium.Map(location=map_center, zoom_start=12)

# Prepare the pickup coordinates for the heatmap
heat_data = [[row['pickup_location_lat'], row['pickup_location_lon']] for index, row in data.iterrows()]

# Create the heatmap
HeatMap(heat_data).add_to(uber_map)

# Save the map
uber_map.save('uber_pickup_heatmap.html')
