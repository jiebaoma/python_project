# from matplotlib import pyplot as plt
# x=range(2,26,2)
# y=[12,13,14,14,5,16.5,18,20,22,17,13.5,20]
# plt.plot(x,y)
# plt.show()

#!/usr/bin/env python
#__*__ coding:utf-8 __*__
from matplotlib import pyplot
years = [1950,1960,1970,1980,1990,2000,2010]
gdb = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

# 创建一幅线图，x轴是年份，y轴是gdb
pyplot.plot(years,gdb,color='red',marker='o',linestyle='solid')
# 添加一个标题
pyplot.title('名义GDP')
# 给y轴加标记
pyplot.xlabel("years")
pyplot.ylabel('十亿美元')
# 输出线图
pyplot.show()
