from matplotlib import pyplot as plt
from matplotlib import font_manager


x = range(11, 31, 1)
y1 = [1, 1, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [2, 1, 4, 0, 2, 1, 2, 1, 2, 1, 1, 2, 3, 2, 1, 4, 1, 0, 2, 3]

# 设置字体，fname表示字体在本地的路径
my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

# figsize表示图片大小，dpi表示分辨率
plt.figure(figsize=(20, 8), dpi=80)

# 绘制折线图,多个图形就多调用几次plot即可,颜色还可以用十六进制代码
plt.plot(x, y1, label="自己", color="#4B0082", linestyle="-", linewidth=2)
plt.plot(x, y2, label="同桌", color="cyan", linestyle="--", linewidth=3)

_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labels, fontproperties=my_font)
plt.yticks(range(0, 9))

# 绘制网格 alpha表示透明度,范围在0~1之间,linestyle表示线条样式
plt.grid(alpha=0.4, linestyle=":")

# 添加图列,只有在legend这里才是用prop，其他地方都是fontproperties来接收my_font
# loc参数表示位置,0~6选择,要显示“自己”和“同桌”必须调用legend方法才行
plt.legend(prop=my_font, loc=0)

# 添加对折线图的描述,xlabel表示对x轴的描述
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("个数", fontproperties=my_font)
plt.title("11岁到30岁每年交的女盆友数量", fontproperties=my_font)

# 保存图片
plt.savefig("./t3.png")

# 展示图片
plt.show()