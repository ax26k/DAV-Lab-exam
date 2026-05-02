import pandas as pd

# Load data
df = pd.read_csv("taxi_data.csv")

# Convert datetime
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Create duration
df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60

# Define "real trip"
clean_df = df[
    (df['trip_distance'] > 0) &
    (df['fare_amount'] > 0) &
    (df['trip_duration'] > 1) &
    (df['passenger_count'] > 0)
]

print("Original rows:", len(df))
print("Cleaned rows:", len(clean_df))

# Save cleaned data
clean_df.to_csv("cleaned_data.csv", index=False)