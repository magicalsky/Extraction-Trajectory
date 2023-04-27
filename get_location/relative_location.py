"""
Get the relative coordinates of MC
"""

from decimal import Decimal
import numpy as np
import pandas as pd


# Set the origin coordinates(door)
x_origin = -1192
y_origin = -246
z_origin = 4

location_list = []
with open(r'../result/merge/merge.txt', encoding='utf-8') as f:
    for line in f:
        peo_id, frame, x, y, z = line.split('/')
        x, y, z = map(Decimal, (x, y, z))
        # Calculate relative coordinates
        relative_x = x - x_origin
        relative_y = y - z_origin
        relative_z = z - y_origin
        # Title columns=['id', 'frame', 'x', 'y', 'z']
        location = [peo_id, frame, relative_x, relative_z, relative_y]
        location_list.append(location)

data = pd.DataFrame(location_list, columns=['id', 'frame', 'x', 'y', 'z'])
print(data)
data.to_csv(r'../result/merge/merge_relative.txt', sep=' ', index=False, header=None)
