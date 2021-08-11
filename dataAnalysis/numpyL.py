import numpy as np

t1 = np.arange(24)
t2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
t1 = t1.reshape((4, 6)).astype("float")
# t3 = np.loadtxt(r"C:\Users\86181\Desktop\工作簿2.csv", delimiter=',', dtype=int, unpack=True)
# t4 = np.loadtxt(r"C:\Users\86181\Desktop\工作簿2.csv", delimiter=',', dtype=int)

# t1 = t1 / 0
# print(t1.shape[0], t1.shape[1])
# print(t1.reshape((t1.shape[0]*t1.shape[1],)))
# print(t3)
# t5 = t4.reshape((10, 5))
# print(t5.mean())   均值
# print(t5.max())   最大值
# print(t5.min())    最小值
# print(np.median(t5)) 中值
# print(np.ptp(t5))   极值
# print(t5.std())  标准值
# print(80*'*')
# print(t5[2, 0:3])

"""
t1 = np.arange(24).reshape((4, 6)).astype('float') nan为浮点型，所以要把整型的数组类型改为float
numpy中的赋值操作：t1[1, 2:] = np.nan
如果t1中没有nan，那么 t1是等于t1的，如果有nan那么
t1[t1!=t1]出现True的就是nan的地方，给出现nan的每一列赋值,col代表每一列
col[col!=col]=
"""

t1[1, 2:] = np.nan   # 把第2行，第3列及以后的数字赋值为nan
t3 = np.count_nonzero(t1 != t1)   # 查看t1中 t1!=t1(即nan出现的地方，因为nan不等于nan) 有几个
for i in range(t1.shape[1]):  # 遍历数组中的每一列
    temp_col = t1[:, i]   # 当前第i列
    nan_num = np.count_nonzero(temp_col != temp_col)  # 不等于说明有nan， 所以数量不为0
    if nan_num != 0:  # 不为0，说明这一列有nan
        temp_not_nan_num = temp_col[temp_col == temp_col]    # 把这一列中不为nan的数值取出来，即这一列中相等的就不为nan， 放在一个新的数组中
        # temp_nan_num = temp_col[temp_col != temp_col]
        temp_col[temp_col != temp_col] = temp_not_nan_num.mean()  # 把当前i列的均值赋值给当前列nan出现的地方
        # temp_col[np.isnan(temp_col)] = temp_not_nan_num.mean()   # 等价于上一列
        # print(temp_col)

print(t1)