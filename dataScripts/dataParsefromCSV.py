#this script was used to seperate the data from a csv file into different csv files based on the district column
import pandas as pd
import os

#change the input as  necessary

input_csv = "./dailyclimate.csv"  
output_folder = "district_csvs"  



if not os.path.exists(output_folder):
    os.makedirs(output_folder)


df = pd.read_csv(input_csv)


if 'District' not in df.columns:
    raise Exception("The dataset does not have a 'District' column. Please check your CSV columns.")


districts = df['District'].unique()


for district in districts:
    df_district = df[df['District'] == district]
    

    filename = district.strip().replace(" ", "_") + ".csv"
    filepath = os.path.join(output_folder, filename)

    df_district.to_csv(filepath, index=False)
    
    print(f"✅ Saved: {filepath} ({len(df_district)} rows)")

print("\n🎉 All district data saved as separate CSV files in the 'district_csvs' folder.")
