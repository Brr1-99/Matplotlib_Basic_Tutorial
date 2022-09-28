import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

plt.figure(figsize=(8,5))

plt.title("Gas Prices in USD by year and country", fontdict={'fontweight': 'bold', 'fontsize': 18})

# Plotting multiple countries data

plt.plot(gas.Year, gas.USA, 'b.-')
plt.plot(gas.Year, gas.Canada, 'r.-')
plt.plot(gas.Year, gas.Australia, 'g.-')

# Factorised way

countries = ['USA', 'Canada', 'Australia']

for country in gas:
    if country in countries:
        plt.plot(gas.Year, gas[country], marker='.')

# Showing the markers every 3 years 

plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('USD')

plt.legend()
plt.show()

plt.savefig('gas_graph.png', dpi=300)