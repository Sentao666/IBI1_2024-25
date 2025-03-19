# Population data of the constituent countries of the UK
uk_population = [57.11, 3.13, 1.91, 5.45]
# Population data of the provinces neighboring Zhejiang
zj_neighbouring_provinces_population = [65.77, 41.88, 45.28, 61.27, 85.15]

# Sort the population data of the UK constituent countries
sorted_uk_population = sorted(uk_population)
# Sort the population data of the provinces neighboring Zhejiang
sorted_zj_provinces_population = sorted(zj_neighbouring_provinces_population)

print("Sorted UK population:", sorted_uk_population)
print("Sorted Zhejiang - neighbouring provinces population:", sorted_zj_provinces_population)

import matplotlib.pyplot as plt

# Population data of the constituent countries of the UK
uk_population = [57.11, 3.13, 1.91, 5.45]
labels_uk = ['England', 'Wales', 'Northern Ireland', 'Scotland']

# Population data of the provinces neighboring Zhejiang
zj_neighbouring_provinces_population = [65.77, 41.88, 45.28, 61.27, 85.15]
labels_zj = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']

# Plot the pie chart for the population distribution in the UK
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.pie(uk_population, labels=labels_uk, autopct='%1.1f%%')
plt.title('Population Distribution in UK Countries')

# Plot the pie chart for the population distribution in the provinces neighboring Zhejiang
plt.subplot(1, 2, 2)
plt.pie(zj_neighbouring_provinces_population, labels=labels_zj, autopct='%1.1f%%')
plt.title('Population Distribution in Zhejiang - Neighbouring Provinces')

plt.show()
