import numpy as np
import matplotlib.pyplot as plt
from numpy import *

data = np.loadtxt('pIC50.txt', dtype=float, usecols=(0,), skiprows=1)
print(data)

plt.hist(data, color='black',edgecolor='white')
plt.show()
