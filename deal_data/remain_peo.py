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
frame_min = 1
frame_max = data['frame'].max()

# print(data)

remain_peo = []
for frame in range(frame_min, frame_max + 1, 1):
    frame_data = data[data.frame == frame]
    remain_peo_data = frame_data[frame_data.x > 0]
    print('Frame {}'.format(frame), len(remain_peo_data))
    frame_peoNum = [frame-1, len(remain_peo_data)]
    remain_peo.append(frame_peoNum)
    remain_data = pd.DataFrame(remain_peo, columns=['frame', 'num'])
    remain_data.to_excel(r'../result/remain_peo_num.xlsx', index=False)
    # print(remind_data)
    print(remain_peo_data)
    print('---------------------------------------------------------')
