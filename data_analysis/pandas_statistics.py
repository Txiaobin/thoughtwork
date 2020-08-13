# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 09:14:10 2020

@author: xiaobin
"""

import pandas as pd

bank = pd.read_csv('bank_data.csv')

from sklearn import datasets
iris = datasets.load_iris()
X=iris().data
y=iris().target           
target_names=iris.target_names      #y的值列表:0:setosa,1:versicolor,2:virginica
feature_names=iris.feature_names    #特征X的名称列表

'''
pdays,previous,poutcome三个字段的字段信息记录缺失。
'''