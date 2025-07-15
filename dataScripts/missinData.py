import pandas as pd
import numpy as np
import os

district= "Jhapa" 

input_csv = f"data/clean_data/{district}_monthly.csv"
output_csv = f"data/final_data/{district}.csv"
missing_fraction = 0.08  # 8% missing randomly
columns_to_corrupt = ['Temp_2m', 'Precip']

df = pd.read_csv(input_csv)

# only get data for 2000 to 2019
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2019)]

# Randomly remove data
np.random.seed(42)  
total_rows = df.shape[0]
num_missing = int(total_rows * missing_fraction)

for col in columns_to_corrupt:
    missing_indices = np.random.choice(df.index, size=num_missing, replace=False)
    df.loc[missing_indices, col] = np.nan
    print(f"✅ Removed {num_missing} entries from '{col}' for interpolation practice.")

os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df.to_csv(output_csv, index=False)

print(f"\n🎉 Saved modified dataset with missing data to '{output_csv}' for your MCSC interpolation demonstration.")
