from matplotlib import pyplot as plt
from matplotlib import font_manager

y1 = [1, 0, 1, 2, 3, 4, 2, 3, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1, 2, 2]
y2 = [2, 1, 1, 0, 0, 1, 1, 2, 1, 3, 3, 2, 2, 5, 5, 4, 6, 3, 2, 5]
x = range(11, 31)
my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y1, label='同桌', color='red', linestyle='-.')
plt.plot(x, y2, label='自己', color='blue', linestyle='--')

_x = list(x)
_xticks_label = ["{}岁".format(i) for i in _x]
plt.xticks(_x, _xticks_label, rotation=0, fontproperties=my_font)
plt.yticks(range(0, 8))

plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("个数", fontproperties=my_font)
plt.title("11到30岁交过的女朋友个数", fontproperties=my_font)
plt.grid(alpha=0.7)

plt.legend(prop=my_font, loc='upper left')

plt.savefig("./2.png")
plt.show()
