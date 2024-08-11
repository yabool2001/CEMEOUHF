import pandas as pd
from pathlib import Path

p = Path('ael')
data_ael = pd.DataFrame()  # Inicjalizacja głównego DataFrame, który będzie zawierał wszystkie dane

for child in p.iterdir () :
    if child.is_file () and child.suffix == '.csv' :
        print ( child )
        data_raw = pd.read_csv ( child , on_bad_lines = 'skip' , delimiter = ',' )
        device_name = child.stem.split('-')[-1].split('_')[0]
        data_raw['Satellite'] = device_name

        # Convert values, forcing errors to NaN
        data_raw['Time (UTCG)'] = pd.to_datetime ( data_raw['Time (UTCG)'] , errors='coerce' )
        data_raw['Azimuth (deg)'] = pd.to_numeric ( data_raw['Azimuth (deg)'] , errors='coerce' )
        data_raw['Elevation (deg)'] = pd.to_numeric ( data_raw['Elevation (deg)'] , errors='coerce' )
        data_raw['Range (lm)'] = pd.to_numeric ( data_raw['Range (km)'] , errors='coerce' )

        # Drop rows where value is NaN
        #data_raw = data_raw.dropna ( subset = ['Time (UTCG)'] )
        #data_raw = data_raw.dropna ( subset = ['Azimuth (deg)'] )
        #data_raw = data_raw.dropna ( subset = ['Elevation (deg)'] )
        #data_raw = data_raw.dropna ( subset = ['Range (km)'] )
        # Usuwanie wierszy z wartościami NaN w interesujących nas kolumnach
        data_raw.dropna ( subset = ['Time (UTCG)' , 'Azimuth (deg)' , 'Elevation (deg)' , 'Range (km)'] , inplace = True )

        # Dodawanie danych z aktualnego pliku do głównego DataFrame
        data_ael = pd.concat ( [data_ael , data_raw] , ignore_index = True )
        print ( data_ael )      

max_elevation = data_ael['Elevation (deg)'].max ()
# Find the row number where the maximum elevation value is located
max_elevation_row_polmeo1 = data_ael[data_ael['Elevation (deg)'] == max_elevation].index[0]

print ( "Maximum Elevation POLMEO1:", max_elevation )
print ( "Row Number :", max_elevation_row_polmeo1 )
print (data_ael.head () )