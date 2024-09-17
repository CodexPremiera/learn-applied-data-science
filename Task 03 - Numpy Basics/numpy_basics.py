import matplotlib.pyplot as plt
import numpy as np

path = './air-quality-data.csv'
np_data = np.genfromtxt(path, delimiter=',', skip_header=True, usecols=range(1, 13))

pm25_column = np_data[::, 1]

plt.plot(pm25_column)
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('PM2.5 Variation')
plt.show()
