import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7)

# histograma
data = np.random.normal(10, 0.5, 5000)
plt.hist(data)
plt.show()

# boxplot
plt.boxplot(data)

# scatter plot
x = np.random.normal(10, 0.5, 100)
y = np.random.uniform(0, 20, 100)

fig = plt.figure()
ax = plt.axes()
ax.scatter(x, y, marker = 'o', color = 'red', label = 'data 1',\
    alpha = 0.5)
ax.scatter(x * 0.5, y * 0.5, marker = 'v', color = 'green',\
    label = 'data 2', alpha = 0.7)
ax.legend()