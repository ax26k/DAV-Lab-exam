import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_data.csv")

# R from ACT 1
R = 5

# Simulate fare increase
df['fare_after'] = df['fare_amount'] * (1 + R/100)

# Tip percentage
df['tip_percent'] = df['tip_amount'] / df['fare_amount']
df['tip_percent_after'] = df['tip_amount'] / df['fare_after']

# Compare averages
before_fare = df['fare_amount'].mean()
after_fare = df['fare_after'].mean()

before_tip = df['tip_percent'].mean()
after_tip = df['tip_percent_after'].mean()

print("Avg Fare Before:", before_fare)
print("Avg Fare After:", after_fare)
print("Avg Tip% Before:", before_tip)
print("Avg Tip% After:", after_tip)

# Plot Fare
plt.figure()
plt.bar(["Before", "After"], [before_fare, after_fare])
plt.title("Average Fare Before vs After Policy")
plt.show()

# Plot Tip %
plt.figure()
plt.bar(["Before", "After"], [before_tip, after_tip])
plt.title("Average Tip % Before vs After Policy")
plt.show()