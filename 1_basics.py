import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating a basic graph with values for x and y coordinate

x = [1, 3, 6]
y = [2, 5, 8]

plt.plot(x,y)
plt.show()

# Custom the graph names and styling them

plt.title('The first of many graphs', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X axis name')
plt.ylabel('Y axis name')

# Changing the steps on the axis

plt.xticks([0,1,2,3])
plt.yticks([2,4,6,8])

# Putting a legend to our graph-lines and styling it

plt.plot(x,y, label='meaning_of_the_line', color='yellow', linewidth=2, marker='.', markeredgecolor='blue', linestyle='--')
plt.legend()

# Shorthand notation to styling the lines

'''
    "[color][marker][line]"
'''
plt.plot(x,y, 'b.--', label='mean of the data')

# Creating graphs whose values are from math functions

x2 = np.arange(0, 4, 0.5)
plt.plot(x2, x2**2, 'r', label='X^2')

# Mid-values change style, e.g. to show the tendency of the function as a dotted graph

plt.plot(x2[:5], x2[:5]**2, 'r')
plt.plot(x2[4:], x2[4:]**2, 'r--')

# Resizing the graph: where dpi means pixels per inch of side

plt.figure(figsize=(4,2), dpi=300)

# Saving a graph

plt.savefig('firstgraph.png', dpi=250)

# Create a bar chart

labels = ['Jan', 'Feb', 'Mar']
values = ['31', '28', '31']

bars = plt.bar(labels, values)

# Set a pattern for the columns

bars[0].set_hatch('/')
bars[1].set_hatch('O')

plt.show()