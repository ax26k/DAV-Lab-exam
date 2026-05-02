import pandas as pd
import os

# 👉 CHANGE THIS PATH (your folder location)
folder_path = r"C:\Users\ub15-lab-004\Downloads\DAV data"

dataframes = []

# 👉 ONLY load correct files (IMPORTANT FIX)
files = [f for f in os.listdir(folder_path) 
         if f.startswith("yellow_tripdata") and f.endswith(".parquet")]

print("Files found:", files)

for file in files:
    try:
        file_path = os.path.join(folder_path, file)
        print(f"Loading {file}...")

        df = pd.read_parquet(file_path)

        dataframes.append(df)

    except Exception as e:
        print(f"Skipping {file} due to error:", e)

# 👉 Combine all data
df = pd.concat(dataframes, ignore_index=True)

print("All files combined!")

# 👉 Convert datetime
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

# 👉 Extract useful columns
df['Hour'] = df['tpep_pickup_datetime'].dt.hour
df['Day'] = df['tpep_pickup_datetime'].dt.day_name()
df['Month'] = df['tpep_pickup_datetime'].dt.month

print("Extracted Hour, Day, Month!")

# 👉 Filter months (April, May, June)
df = df[(df['Month'] >= 4) & (df['Month'] <= 6)]

print("Filtered months 4–6!")

# 👉 Save clean data
output_path = os.path.join(folder_path, "cleaned_data.csv")
df.to_csv(output_path, index=False)

print("Saved as cleaned_data.csv")