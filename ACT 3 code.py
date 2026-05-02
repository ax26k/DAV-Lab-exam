import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

# Extract hour
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['Hour'] = df['tpep_pickup_datetime'].dt.hour

# Trip count by hour
hourly = df.groupby('Hour').size()

plt.figure()
plt.plot(hourly.index, hourly.values)
plt.title("Trip Volume by Hour")
plt.xlabel("Hour")
plt.ylabel("Trips")
plt.show()