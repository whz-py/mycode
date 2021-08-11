import matplotlib.pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

x_3 = range(1, 32)
x_10 = range(51, 82)
y1 = [1, 2, 5, 6, 9, 7, 4, 5, 7, 10, 8, 4, 19, 12, 20, 6, 1, 5, 8, 10, 12, 14, 16, 19, 20, 17, 18, 24, 21, 26, 29]
y2 = [30, 29, 28, 25, 22, 26, 27, 21, 32, 21, 31, 22, 23, 25, 21, 18, 19, 18, 16, 15, 16, 15, 13, 10, 5, 1, 10, 9, 6, 13, 4]

plt.figure(figsize=(20, 8), dpi=80)

plt.scatter(x_3, y1, label="3月份温度", color="b")
plt.scatter(x_10, y2, label="10月份温度", color="cyan")

_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)


plt.grid(alpha=0.4)

plt.xlabel("日期", fontproperties=my_font)
plt.ylabel("温度 单位(℃)", fontproperties=my_font)
plt.title("3月份和10月份温度对比", fontproperties=my_font)

plt.legend(prop=my_font, loc=2)

plt.savefig("./temp.png")

plt.show()
