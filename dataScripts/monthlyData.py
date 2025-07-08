#this script aggregates daily climate data into monthly averages and sums for a specific district.
import pandas as pd

#change as per need
district = "Kathmandu"  
input_csv = f"district_csvs/{district}.csv"
output_csv = f"monthly_csvs/{district}Kathmandu_monthly.csv"

import os
os.makedirs("monthly_csvs", exist_ok=True)

df = pd.read_csv(input_csv, parse_dates=['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

monthly_df = df.groupby(['Year', 'Month', 'District']).agg({
    'Temp_2m': 'mean',
    'Precip': 'sum',
    'MaxTemp_2m': 'mean',
    'MinTemp_2m': 'mean',
    'Humidity_2m': 'mean',
    'Pressure': 'mean'
}).reset_index()

monthly_df.to_csv(output_csv, index=False)

print(f"✅ Saved monthly aggregated data to {output_csv}")
