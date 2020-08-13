# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:24:27 2020

@author: xiaobin
"""

'''
忽略数据标准化,使用Kmeans聚类,设定k值为3,输出所有样本点的聚类结果,3个类别的类均值
尝试以花萼长度(sepal length),花瓣长度(petal length)为x,y轴,可视化聚类结果
'''

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

iris = datasets.load_iris()
X=iris.data         
feature_names=iris.feature_names    #特征X的名称列表

mykmeans = KMeans(n_clusters=3)
y_pred = mykmeans.fit_predict(X)
centers = mykmeans.cluster_centers_
print(y_pred,centers)

plt.scatter(X[:, 0], X[:, 2], c=y_pred)
plt.show()