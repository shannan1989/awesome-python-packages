#!/usr/bin/env python
# coding=utf-8

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 定义图的大小
plt.figure(figsize=(16, 8))

# 创建地图
m = Basemap()
# 画上海岸线
m.drawcoastlines()
# 画上国家
m.drawcountries(linewidth=1.5)

plt.show()
