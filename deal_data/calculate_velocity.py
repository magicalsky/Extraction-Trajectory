"""
Calculate the speed, calculate the speed of all people
"""

step = 4

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

text = pd.read_table(r'../result/merge/merge_relative.txt', header=None, sep=' ')
data1 = pd.DataFrame({
    'id': text[0],
    'frame': text[1],
    'x': text[2],
    'y': text[3]
})
for peo in range(1, 21):
    data = data1[data1.id == peo]
    # print(data)
    t_max = data['frame'].max()
    print(t_max)
    t_min = data['frame'].min()
    t = list(range(t_min, t_max + 1))

    V = []

    for i in t:
        data_t = data[data.frame == i]
        data_t_before = data[data.frame == (i - step)]
        data_t_after = data[data.frame == (i + step)]
        if i - step >= t_min:
            x_t_before = float(np.array(data_t_before.x))
            y_t_before = float(np.array(data_t_before.y))
        else:
            x_t_before = float(np.array(data_t.x))
            y_t_before = float(np.array(data_t.y))
        if i + step <= t_max:
            x_t_after = float(np.array(data_t_after.x))
            y_t_after = float(np.array(data_t_after.y))
        else:
            x_t_after = float(np.array(data_t.x))
            y_t_after = float(np.array(data_t.y))

        vi = ((((x_t_after - x_t_before) ** 2) + ((y_t_after - y_t_before) ** 2)) ** 0.5) / (
                    (2 * step) / 30)
        V.append(vi)

    plt.plot(t, V)

    plt.xlim(0, 200)
    plt.ylim(0, 2)
    plt.ylabel('v[m/s]')
    plt.xlabel('t[frame]')
    plt.title('{}Velocity-Time'.format(peo))
    plt.show()
    # print(V)
