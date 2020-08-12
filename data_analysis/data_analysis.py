# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:32:46 2020

@author: xiaobin
"""

'''
使用pandas读取此数据集的内容，并统计得到以下信息：
1.一共有多少不同的用户
2.一共有多少不同的电影
3.一共有多少不同的电影种类
4.一共有多少电影没有外部链接
5.2018年一共有多少人进行过电影评分
6.2018年评分5分以上的电影及其对应的标签
7.绘制电影复仇者联盟（The Avengers）每个月评分的平均值变化曲线图
'''

import pandas as pd

ratings = pd.read_csv('date/ml-latest-small/ratings.csv',index_col=None)
tags = pd.read_csv('date/ml-latest-small/tags.csv',index_col=None)
movies = pd.read_csv('date/ml-latest-small/movies.csv',index_col=None)
#link = pd.read_csv('date/ml-latest-small/link.csv',index_col=None)
#genome_scores = pd.read_csv('date/ml-latest-small/genome_scores.csv',index_col=None)
#genome_tags = pd.read_csv('date/ml-latest-small/genome_tags.csv',index_col=None)

usernum = ratings.groupby(['userId'])