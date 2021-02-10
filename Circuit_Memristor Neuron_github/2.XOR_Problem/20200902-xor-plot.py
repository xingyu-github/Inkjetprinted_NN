# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 21:25:18 2020

@author: duxingyu8
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2
##
#vegetables = ["10^7", "10^6", "10^5", "10^4",
#              "10^3", "10^2", "10^1", "10^0", "10^-1", "10^-2", "10^-3"]
#farmers = ["10^-3", "10^-2", "10^-1",
#           "10^0", "10^1", "10^2", "10^3", "10^4", "10^5", "10^6"]
vegetables = ["10^-3", "10^-2", "10^-1",
           "10^0", "10^1", "10^2", "10^3", "10^4", "10^5", "10^6"]
#farmers = ["10^-3", "10^-2", "10^-1",
#           "10^0", "10^1", "10^2", "10^3", "10^4", "10^5", "10^6"]

##use different Rin
farmers = ["10^-1","10^0", "10^1", "10^2", "10^3", "10^4", "10^5", "10^6","10^7", "10^8"]


fig, ax = plt.subplots()
im = ax.imshow(minus)

plt.colorbar(im)
# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)
plt.tick_params(axis='x', labelsize=8)    # 设置x轴标签大小
plt.tick_params(axis='y', labelsize=8)    # 设置x轴标签大小
plt.xticks(rotation=-45)    # 设置x轴标签旋转角度

#
## Rotate the tick labels and set their alignment.
#plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#         rotation_mode="anchor")
##
## Loop over data dimensions and create text annotations.
#for i in range(len(vegetables)):
#    for j in range(len(farmers)):
#        text = ax.text(j, i, a[i, j],
#                       ha="center", va="center", color="w")
# Add title and labels to plot.
plt.title('Heatmap of Output one minus Output zero')
#plt.xlabel('Gamma:Rground/Rinput')
plt.ylabel('Lambda: Routput/Rinput')
plt.xlabel('Rinput (ohms)')

plt.show()