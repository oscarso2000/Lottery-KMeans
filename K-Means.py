import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Importing the dataset
data = pd.read_csv('Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv')
print(data.shape)

# Getting the values and plotting it
x = data['Multiplier'].values
y = data['Mega Ball'].values
X = np.array(list(zip(x, y)))
plt.scatter(x, y, c='black', s=1)
plt.show()


print("DONE")