from matplotlib import pyplot as plt
from matplotlib import font_manager

'''
直方图可以自动的统计原始数据。
'''


a = [30, 29, 28, 25, 22, 26, 27, 21, 32, 21, 31, 22, 23, 25, 21, 18, 19, 18, 16, 15, 16, 15, 13, 10, 5, 2, 10, 9, 6, 13, 4]

d = 3
num_bins = (max(a)-min(a))//d
print(max(a)-min(a))

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(a, num_bins)
plt.xticks(range(min(a), max(a)+d, d))

plt.grid(alpha=0.4)

plt.show()