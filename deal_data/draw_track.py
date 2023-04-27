"""
Mapping pedestrian trajectories
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

text = pd.read_table(r'../result/merge/merge_relative.txt', header=None, sep=' ')
data = pd.DataFrame({
    'id': text[0],
    'frame': text[1],
    'x': text[2],
    'y': text[3]
})

print(data)
# Get peo_id, take the first frame of data, get the id value
frame1_data = data[data.frame == 1]
peo_id_list = np.array(frame1_data.id)

# Mapping the trajectory of each individual
plt.style.use('ggplot')
for peo_id in peo_id_list:
    peo_id_data = data[data.id == peo_id]
    x = peo_id_data['x']
    y = peo_id_data['y']
    # plt.plot(x, y, label=peo_id)
    plt.plot(x, y)
    # plt.xlim(0, 13)
    # plt.ylim(10, 0)
    plt.ylabel('y[m]')
    plt.xlabel('x[m]')
    plt.title('Trajectory')
    # plt.xticks(np.linspace(0, 13, 14))
    # plt.yticks(np.linspace(10, 0, 11))
    # plt.legend(loc=0)
plt.show()