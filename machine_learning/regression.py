# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:24:27 2020

@author: xiaobin
"""

'''
画出RM,DIS,PTRATIO,LSTAT与y的散点图,分析特征与y是否有线性关系?
尝试进行线性回归,使用RM,DIS,PTRATIO,LSTAT预测房价y,写出回归方程
解释下RM与Y的关系?
对某新小区,其RM=8,DIS=2,PTRATIO=12,LSTAT=22,预测该小区房价
'''

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

boston = datasets.load_boston()
x = boston['data']
y = boston['target']
x = x[:,[5,7,10,12]]

fig1, ax1 = plt.subplots()
ax1.plot(x[:,0], y, marker='o', linestyle='', ms=5, label = 'x')
plt.xlabel("RM")
plt.ylabel("Y")
ax1.legend()

fig2, ax2 = plt.subplots()
ax2.plot(x[:,1], y, marker='o', linestyle='', ms=5, label = 'x')
plt.xlabel("RM")
plt.ylabel("Y")
ax2.legend()

fig3, ax3 = plt.subplots()
ax3.plot(x[:,2], y, marker='o', linestyle='', ms=5, label = 'x')
plt.xlabel("RM")
plt.ylabel("Y")
ax3.legend()

fig4, ax4 = plt.subplots()
ax4.plot(x[:,3], y, marker='o', linestyle='', ms=5, label = 'x')
plt.xlabel("RM")
plt.ylabel("Y")
ax4.legend()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
myregression = LinearRegression()
myregression.fit(x_train, y_train)
y_predict = myregression.predict(x_test)

w = myregression.coef_
b = myregression.intercept_
print("y = %f*x1 + %f*x2 + %f*x3 + %f*x4 + %f" % (w[0], w[1], w[2], w[3], b))


a = [8,2,12,22]
print(myregression.predict([[8,2,12,22]]))


'''
由RM与Y的散点图可以看出，RM与Y近似于一次线性关系。
'''