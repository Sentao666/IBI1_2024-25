# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory
os.chdir("F:\IBI(ZST)\IBI1_2024-25\Practical10")

# Print current working directory and files
print(os.getcwd())
print(os.listdir())

# Load DALYs data from CSV
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show first 5 rows and basic info
print(dalys_data.head(5))
dalys_data.info()
print(dalys_data.describe())

# Extract year column for first 10 rows
year_column_first_10_rows = dalys_data.iloc[0:10, 2]
print(year_column_first_10_rows)

# Filter data for year 1990
is_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[is_1990, 'DALYs']
print(dalys_1990)

# Compare UK and France DALYs
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"]
france = dalys_data.loc[dalys_data.Entity == "France", "DALYs"]
uk_mean = uk.mean()
france_mean = france.mean()
print(f"Average DALYs in the United Kingdom: {uk_mean}")
print(f"Average DALYs in France: {france_mean}")

# Plot UK DALYs over time
uk_data = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.plot(uk_data.Year, uk_data.DALYs, 'b+')
plt.xticks(uk_data.Year, rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Change in DALYs over time in the United Kingdom')
plt.show()

# Compare China and UK DALYs over time
china_uk_data = dalys_data.loc[dalys_data.Entity.isin(["China", "United Kingdom"]), ["Year", "Entity", "DALYs"]]
china_data = china_uk_data.loc[china_uk_data.Entity == "China", ["Year", "DALYs"]]
uk_data = china_uk_data.loc[china_uk_data.Entity == "United Kingdom", ["Year", "DALYs"]]

plt.figure(figsize=(10, 6))
plt.plot(china_data.Year, china_data.DALYs, label='China', marker='o')
plt.plot(uk_data.Year, uk_data.DALYs, label='United Kingdom', marker='s')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('Change in DALYs over time in China and the United Kingdom')
plt.legend()
plt.xticks(rotation=-90)
plt.show()