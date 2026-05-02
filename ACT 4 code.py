import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['Hour'] = df['tpep_pickup_datetime'].dt.hour
df['Month'] = df['tpep_pickup_datetime'].dt.month

# Pattern 1: Trips by hour
hourly = df.groupby('Hour').size()

plt.figure()
plt.plot(hourly.index, hourly.values)
plt.title("Trip Volume by Hour")
plt.xlabel("Hour")
plt.ylabel("Trips")
plt.show()

# Pattern 2: Average fare by hour
fare_hour = df.groupby('Hour')['fare_amount'].mean()

plt.figure()
plt.plot(fare_hour.index, fare_hour.values)
plt.title("Average Fare by Hour")
plt.xlabel("Hour")
plt.ylabel("Fare")
plt.show()

# Pattern 3: Trips by month
monthly = df.groupby('Month').size()

plt.figure()
plt.plot(monthly.index, monthly.values)
plt.title("Trip Volume by Month")
plt.xlabel("Month")
plt.ylabel("Trips")
plt.show()