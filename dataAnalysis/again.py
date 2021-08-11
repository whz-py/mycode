import random

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")
y = [random.randint(20, 35) for i in range(120)]
x = range(0, 120)

plt.figure(figsize=(24, 8), dpi=80)

plt.plot(x, y)

_x = list(x)[::3]
_xticks_lable = ["10点{}分".format(i) for i in range(60)]
_xticks_lable += ["11点{}分".format(i) for i in range(60+3)]

plt.xticks(_x, _xticks_lable[::3], rotation=45, fontproperties=my_font)
# plt.yticks(y)
plt.savefig('./again.png')

plt.show()
