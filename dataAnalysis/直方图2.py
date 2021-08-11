from matplotlib import pyplot as plt
from matplotlib import font_manager

'''
这是条形图，用于统计经过统计后的数据。
直方图只能统计没有统计过的数据。
'''

my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
# width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]  # 这个参数也没用到
quantity = [836, 2797, 3723, 3923, 3596, 1495, 3275, 354, 824, 316, 512, 47]

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(range(12), quantity, width=1)  # 默认width是0.8 增加了0.2就挨在一起了
_x = [i - 0.5 for i in range(13)]
_xticks_labels = interval + [150]
plt.xticks(_x, _xticks_labels)

plt.grid(alpha=0.4)
plt.show()
