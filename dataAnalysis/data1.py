import numpy as np
import pandas as pd
from collections import Counter

from matplotlib import pyplot as plt

df = pd.read_csv('./BeijingPM20100101_20151231.csv')
# print(df.info())
# print(df.head(5))
peroid = pd.PeriodIndex(year=df['year'], month=df['month'], day=df['day'], hour=df['hour'], freq='H')
df['datetime'] = peroid

df.set_index('datetime', inplace=True)
df = df.resample('7D').mean()  # 每隔7天采样，取均值
print(df['PM_US Post'])
# data = df['PM_US Post'].dropna()   # 把PM_US Post这一列的nan全都删除
# _x = data.index
# _x = [i.strftime("%Y%m%d") for i in _x]
# # print(_x)
# _y = data.values
#
# plt.figure(figsize=(20, 8), dpi=80)
# plt.plot(range(len(_x)), _y)
# plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)
# plt.show()

# a = [2, 3, 4, 4,6,8,9]
# b = [3, 4, 4, 4,7,8,9]
# res = np.intersect1d(a, b)
# print(res)
# ca = Counter(a)
# print(ca)
# cb = Counter(b)
# print(cb)
# pt = list(map(lambda x: min(ca[x], cb[x]), res))
# print(pt)
# result = np.repeat(res, pt)
# print(result)