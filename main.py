import pandas as pd
import numpy as np
from pathlib import Path

file_path = 'ael/Place-CEMID-Sensor-Sensor1-To-Satellite-POLMEO11_AER.csv'

p = Path('ael')
for child in p.iterdir () :
    print ( child )
    data_raw = pd.read_csv ( child , on_bad_lines = 'skip' , delimiter = ',' )

data = data_raw
# Convert values, forcing errors to NaN
data['Time (UTCG)'] = pd.to_datetime ( data['Time (UTCG)'] , errors='coerce' )
data['Azimuth (deg)'] = pd.to_numeric ( data['Azimuth (deg)'] , errors='coerce' )
data['Elevation (deg)'] = pd.to_numeric ( data['Elevation (deg)'] , errors='coerce' )
data['Range (lm)'] = pd.to_numeric ( data['Range (km)'] , errors='coerce' )

# Drop rows where value is NaN
data = data.dropna ( subset = ['Time (UTCG)'] )
data = data.dropna ( subset = ['Azimuth (deg)'] )
data = data.dropna ( subset = ['Elevation (deg)'] )
data = data.dropna ( subset = ['Range (km)'] )

max_elevation = data['Elevation (deg)'].max ()

# Find the row number where the maximum elevation value is located
max_elevation_row_polmeo1 = data[data['Elevation (deg)'] == max_elevation].index[0]

print ( "Maximum Elevation POLMEO1:", max_elevation )
print ( "Row Number POLMEO1:", max_elevation_row_polmeo1 )

print ( data['Time (UTCG)'][0] )