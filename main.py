import pandas as pd
from pathlib import Path

p = Path('ael')
df = pd.DataFrame()  # Inicjalizacja głównego DataFrame, który będzie zawierał wszystkie dane

for child in p.iterdir () :
    if child.is_file () and child.suffix == '.csv' :
        print ( child )
        df_ael = pd.read_csv ( child , on_bad_lines = 'skip' , delimiter = ',' )
        device_name = child.stem.split('-')[-1].split('_')[0]
        df_ael['Satellite'] = device_name

        # Convert values, forcing errors to NaN
        df_ael['Time (UTCG)'] = pd.to_datetime ( df_ael['Time (UTCG)'] , errors='coerce' )
        df_ael['Azimuth (deg)'] = pd.to_numeric ( df_ael['Azimuth (deg)'] , errors='coerce' )
        df_ael['Elevation (deg)'] = pd.to_numeric ( df_ael['Elevation (deg)'] , errors='coerce' )
        df_ael['Range (lm)'] = pd.to_numeric ( df_ael['Range (km)'] , errors='coerce' )

        # Drop rows where value is NaN
        #df_ael = df_ael.dropna ( subset = ['Time (UTCG)'] )
        #df_ael = df_ael.dropna ( subset = ['Azimuth (deg)'] )
        #df_ael = df_ael.dropna ( subset = ['Elevation (deg)'] )
        #df_ael = df_ael.dropna ( subset = ['Range (km)'] )
        # Usuwanie wierszy z wartościami NaN w interesujących nas kolumnach
        df_ael.dropna ( subset = ['Time (UTCG)' , 'Azimuth (deg)' , 'Elevation (deg)' , 'Range (km)'] , inplace = True )

        # Dodawanie danych z aktualnego pliku do głównego DataFrame
        df = pd.concat ( [df , df_ael] , ignore_index = True )
        print ( df )      

max_elevation = df['Elevation (deg)'].max ()
# Find the row number where the maximum elevation value is located
max_elevation_row_polmeo1 = df[df['Elevation (deg)'] == max_elevation].index[0]

print ( "Maximum Elevation POLMEO1:", max_elevation )
print ( "Row Number :", max_elevation_row_polmeo1 )
print ( df.head () )