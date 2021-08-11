import matplotlib.pyplot as plt
from matplotlib import font_manager

a = ["战狼2", "哪吒之魔童降世", "流浪地球","复仇者联盟4：终局之战","红海行动","美人鱼","唐人街探案2","我和我的祖国","我不是药神","中国机长","速度与激情8","西虹市首富","速度与激情7","捉妖记","复仇者联盟3：无限战争","捉妖记2","羞羞的铁拳","变形金刚4：绝迹重生","海王"]
b= [56.39,49.34,46.18,42.05,36.22,33.9,33.71,31.02,30.75,28.76,26.49,25.27,24.26,24.21,23.7,22.19,21.9,21.83,19.97]

my_font = font_manager.FontProperties(fname="C:\WINDOWS\FONTS\MSYH.TTC")

plt.figure(figsize=(20, 8), dpi=80)

plt.barh(range(len(a)), b, linewidth=0.4, color="p")

plt.yticks(range(len(a)), a, fontproperties=my_font)

plt.grid(alpha=0.4)

plt.legend(prop=my_font)

plt.xlabel("票房",fontproperties=my_font)
plt.ylabel("电影名",fontproperties=my_font)
plt.title("票房柱状图", fontproperties=my_font)

plt.savefig("./t4.png")

plt.show()

