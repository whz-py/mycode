# -*- coding=utf-8 -*- #

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# df = pd.read_csv('./starbucks_store_worldwide.csv')
# print(df.info())
# grouped1 = df.groupby(by=[df['Country'], df['State/Province']])[['Brand']].count()  # 两个中括号，结果返回的是dataframe
# grouped2 = df[['Brand']].groupby(by=[df['Country'], df['State/Province']]).count()  # 两个中括号，结果返回的是dataframe
# grouped3 = df.groupby(by=[df['Country'], df['State/Province']]).count()['Brand']   # 1个中括号，结果返回的是Series
# print(grouped1, type(grouped1))
# print('*'*100)
# print(grouped2, type(grouped2))
# print('*'*100)
# print(grouped3, type(grouped3))

df = pd.read_csv('./911.csv')
# print(df.head())
# print(df.title, type(df.title))
# print(df['title'])
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
# print(df)
temp_list = df['title'].str.split(':').tolist()
# cate_list = list(set(i[0] for i in temp_list))
cate_list = list(i[0] for i in temp_list)
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0], 1)))  # 添加一列新的cate
# print(df)
df.set_index('timeStamp', inplace=True)
# grouped = df.groupby(by='cate').count()['title']  # 按照cate这一列分类，并统计所有列出现的次数，['title']是指仅仅列出这一列
plt.figure(figsize=(20, 8), dpi=80)
for group_name, group_data in df.groupby(by='cate'):
    # print(group_name, group_data)
    count_month = group_data.resample('M').count()['title']
    # print(count_month)
    _x = count_month.index
    _x = [i.strftime("%Y%m%d") for i in _x]
    print(_x)
    _y =count_month.values
    plt.plot(range(len(_x)), _y, label=group_name)
plt.xticks(range(len(_x)), _x, rotation=45)
plt.show()

# zero_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
# print(zero_df['EMS'])
# for i in cate_list:   # 遍历分类的列表。['', '', '']
#     zero_df[i][df['title'].str.contains(i)] = 1   # 给zero_df赋值，df['title']这一列包含i的都赋值为1
#     print(zero_df)
#     break
#
