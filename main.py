import pandas as pd
from pathlib import Path

file_path = 'ael/Place-CEMID-Sensor-Sensor1-To-Satellite-POLMEO11_AER.csv'

p = Path('ael')
for child in p.iterdir () :
    print ( child )
    data_raw = pd.read_csv ( child , on_bad_lines = 'skip' )

data_polmeo1 = data_raw
# Convert the 'Elevation (deg)' column to numeric, forcing errors to NaN
data_polmeo1['Elevation (deg)'] = pd.to_numeric ( data_polmeo1['Elevation (deg)'] , errors='coerce' )

# Drop rows where 'Elevation (deg)' is NaN
data_polmeo1 = data_polmeo1.dropna ( subset = ['Elevation (deg)'] )

max_elevation_polmeo1 = data_polmeo1['Elevation (deg)'].max ()

# Find the row number where the maximum elevation value is located
max_elevation_row_polmeo1 = data_polmeo1[data_polmeo1['Elevation (deg)'] == max_elevation_polmeo1].index[0]

print ( "Maximum Elevation POLMEO1:", max_elevation_polmeo1)
print ( "Row Number POLMEO1:", max_elevation_row_polmeo1 )