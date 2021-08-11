import numpy as np
import pandas as pd
import pymysql
from pymongo import MongoClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# t1 = np.arange(12).reshape((3, 4)).astype('float')
# t2 = np.arange(24).reshape((4, 6))
# # t3 = np.vstack((t1, t2))
# # t4 = np.hstack((t1, t2))
# # t1[:, [0, 3]] = t1[:, [3, 0]]
# # t2[[1, 3], 0:3] = t2[[3, 1], 0:3]
# # print(t1)
# print(id(t1))
#
# t4 = t1
# t3 = t1[:]
# t5 = t1.copy()
# print(id(t3))
# print(id(t4))
# print(id(t5))

# connect = pymysql.connect(host='localhost', user='root', password='5201314', db='ddd')
# cusor = connect.cursor()
# DBsession = sessionmaker(bind=engine)
# sql = 'select * from students'

# data = pd.read_sql(sql, connect)
temp_list = [['A'], ['B'], ['C'], ['D'], ['E']]
gen_list = [i for j in temp_list for i in j]
t3 = pd.DataFrame(np.arange(24).reshape((4, 6)), index=list('abcd'), columns=list('UVWXYZ'))
zeros = pd.DataFrame(np.zeros((t3.shape[0], len(gen_list))),columns=gen_list)
zeros.loc[1, ['A', 'C', 'E']] = 1
print(zeros['A'])

# print(zeros)
# z = zeros.loc[1:3]
# print(z)
# for i in range(t3.shape[0]):
#     zeros.loc[i, temp_list[i]] = 1
# print(zeros)


# t1[:, 1] = np.nan
# num = np.count_nonzero(t1!=t1)
# for i in range(t1.shape[0]):
#     temp_index = t1[i, :]
#     temp_index_num = temp_index[temp_index == temp_index]
#     temp_index[temp_index != temp_index] = temp_index_num.mean()
# print(t1)
# t1[t1!=t1] = np.
# print(t1)
# print(num)

# df1 = pd.DataFrame(np.arange(8).reshape((2, 4)).astype('float'), index=list('AB'), columns=list('wxyz'))
# df2 = pd.DataFrame(np.arange(9).reshape((3, 3)).astype('float'), columns=list('fax'))
# df1.loc['A':'B','x'] = 0
# df2.loc[1, 'x'] = 0
# print(df1)
# print(df2)
# print(df1.merge(df2, on='x', how='outer'))
# print(df1.merge(df2, on='x', how='inner'))
# print(df1.merge(df2, on='x', how='left'))
# print(df1.merge(df2, on='x', how='right'))

# print(df2.join(df1))