from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# 设置字体，这种方法并没有效果
# font = {'family': 'MicroSoft Yahei UI',
#         'weight': 'bold'
#         #'size': 'Regular'
#         }
# matplotlib.rc("font", **font)
# matplotlib.rc("font", family='MicroSoft Yahei UI', weight='bold')

# 设置字体，fname中传的是字体在当前电脑上的路径
my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(0, 120)]
# 设置图片大小
plt.figure(figsize=(15, 8), dpi=70)
# 绘制图片
plt.plot(x, y)

# 将x转换为列表
_x = list(x)
# 设置变量，设置显示的的文字
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# 设置间隔
plt.xticks(_x[::5], _xtick_labels[::5], rotation=45, fontproperties=my_font)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度 单位(℃)", fontproperties=my_font)
plt.title("10点到12点每分钟气温变化图", fontproperties=my_font)

plt.grid(4)
#保存图片
plt.savefig("./t2.png")

plt.show()