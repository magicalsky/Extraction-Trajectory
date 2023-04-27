import os
from decimal import Decimal
import pandas as pd

file_list = os.listdir(r'../result/location_result')

print(file_list)

with open('../result/merge/merge.txt', 'a') as w:
    for file in file_list:
        path = r'../result/location_result/'+file
        with open(path, encoding='utf-8') as f:
            for line in f:
                w.write(line)


