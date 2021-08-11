from matplotlib import pyplot as plt

# 绘制一天中每隔2小时的气温
x = range(2, 26, 2)
y = [13, 14.5, 16, 15, 19, 21, 23, 22.5, 25, 23.5, 20, 18]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置x轴的刻度
_xtick_labels = [i/2 for i in range(4, 49)]
plt.xticks(_xtick_labels)
# plt.xticks(x[::3])   通过步长设置间隔

# 设置y轴上的刻度
plt.yticks(range(min(y), max(y)+2))

# 保存图片
plt.savefig("./t1.png")

# 展示图形
plt.show()