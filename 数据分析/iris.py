# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:22:10 2020

@author: xiaobin
"""

import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('date/iris.csv')

groups = iris.groupby('Name')

fig1, ax1 = plt.subplots()
for name, group in groups:
    ax1.plot(group.SepalLength, group.SepalWidth, marker='o', linestyle='', ms=5, label=name)
plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
ax1.legend()

fig2, ax2 = plt.subplots()
for name, group in groups:
    ax2.plot(group.SepalLength, group.SepalWidth, marker='o', linestyle='', ms=5, label=name)
plt.xlabel("SepalLength")
plt.ylabel("SepalWidth")
ax2.legend()

plt.show()