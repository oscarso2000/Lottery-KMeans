import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Importing the dataset
data = pd.read_csv('iris.csv')
print(data.shape)

# Getting the values and plotting it
x = data['sepal_length'].values
y = data['sepal_width'].values
X = np.array(list(zip(x, y)))
plt.scatter(x, y)
plt.show()


print("DONE")