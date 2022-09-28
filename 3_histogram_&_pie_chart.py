import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

# Create boundaries of data for the histogram

bins = [40,50,60,70,80,90,100]

plt.hist(fifa['Overall'], bins=bins, color='red')

plt.xticks(bins)

plt.ylabel('Number of players')
plt.xlabel('Card points')
plt.title('Distribution of Players by their Points')

plt.show()

# Creating a Pie chart for the preferred foot of all players

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]

plt.pie([left, right], labels=['Left', 'Right'], colors=['#abedfc', '#edeaba'], autopct='%.2f %%')

plt.title('Foot Preferrence of Fifa Players')

plt.show()

# Creating a Pie chart for the weight of all players

# Formating the weight column to be suitable for ploting it

fifa['Weight'] = [int(x.strip('lbs')) if type(x) == str else x for x in fifa['Weight']]

plt.style.use('ggplot')

# Filtering the players by its category

light = fifa.loc[fifa['Weight'] < 125].count()[0]
light_medium = fifa.loc[(fifa['Weight'] >= 125) & (fifa['Weight'] < 150)].count()[0]
medium = fifa.loc[(fifa['Weight'] >= 150) & (fifa['Weight'] < 175)].count()[0]
medium_heavy = fifa.loc[(fifa['Weight'] >= 175) & (fifa['Weight'] < 200)].count()[0]
heavy = fifa.loc[fifa['Weight'] >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Under 125', '125-150', '150-175', '175-200', 'Over 200']
explode = (.4, .2, 0, 0, .4)

plt.title('Weight Distribution of FIFA Players in lbs')

plt.pie(weights, labels=labels, autopct="%.2f %%", pctdistance=0.8, explode=explode)

plt.show