import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置字体
my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

# 数据
a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_14 = [2358, 399, 2358, 365]
b_15 = [12357, 156, 2046, 168]
b_16 = [15789, 325, 2541, 365]
# 设置图片大小和分辨率
plt.figure(figsize=(20, 8), dpi=80)

# 设置条形宽度
width_bar = 0.2
# 设置x_14,x_15,x_16的位置
x_14 = list(range(len(a)))
x_15 = [i+width_bar for i in x_14]   # x_15的位置要往右移动x_14条形宽度的长度
x_16 = [i+width_bar*2 for i in x_14]  # x_16的位置要往右移动x_14和x_15两个加起来的长度
# 开始绘制条形图，并设置图例
plt.bar(range(len(a)), b_14, width=width_bar, label="9月14日票房", color="r")
plt.bar(x_15, b_15, width=width_bar, label="9月15日票房", color="y")
plt.bar(x_16, b_16, width=width_bar, label="9月16日票房", color="cyan")

# 在x轴上设置刻度
plt.xticks(x_15, a, fontproperties=my_font)

# 设置网格和图例
plt.grid(alpha=0.3)
plt.legend(prop=my_font)

# 添加描述信息
plt.xlabel("电影名", fontproperties=my_font)
plt.ylabel("票房(单位:万元)", fontproperties=my_font)
plt.title("三天的票房对比", fontproperties=my_font)

plt.savefig("./t5.png")

plt.show()
