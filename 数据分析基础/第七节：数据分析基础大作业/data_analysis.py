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
import math
import datetime
import matplotlib.pyplot as plt

tag = pd.read_csv('ml-25m/tags.csv')
rating = pd.read_csv('ml-25m/ratings.csv')
movie = pd.read_csv('ml-25m/movies.csv')
link = pd.read_csv('ml-25m/links.csv')
genome_scores = pd.read_csv('ml-25m/genome-scores.csv')
genome_tags = pd.read_csv('ml-25m/genome-tags.csv')

# 根据用户id的不同来判断有多少不同的用户
users_num = (tag['userId'].append(rating['userId'])).nunique()  

# 根据电影id的不同来判断有多少不同的电影
movies_num = movie['movieId'].nunique()  

# 根据电影标签的不同来判断有多少电影种类
genres = []
for i in range(len(movie)):
    genres.extend(movie['genres'][i].split('|'))
genres_num = pd.Series(genres).nunique()  

# 没有外部链接的电影个数
idx = []
for i in range(len(link)):
    if math.isnan(link['tmdbId'][i]):
        idx.append(i)
no_link_num = pd.Series(idx).nunique()  

# 2018年进行过电影评分的人数
time_start = (pd.to_datetime('2018-01-01') - pd.to_datetime('1970-01-01')).total_seconds()
time_end = (pd.to_datetime('2019-01-01') - pd.to_datetime('1970-01-01')).total_seconds()
rating_2018 = rating[(rating['timestamp'] >= time_start) & (rating['timestamp'] < time_end)]
users_2018_rating_num = rating_2018['userId'].nunique()

# 前五题数据的输出
print('不同的用户数：' + str(users_num))
print('不同的电影数：' + str(movies_num))
print('不同的电影种类数：' + str(genres_num))
print('没有外部链接的电影数：' + str(no_link_num))
print('2018年进行过电影评分的用户数：' + str(users_2018_rating_num))

# 2018年评分5分以上的电影及其对应的标签
rating_2018 = rating[(rating['timestamp'] >= time_start) & (rating['timestamp'] < time_end)]
rating_2018_temp = rating_2018[['movieId','rating']]
movie_temp = movie[['movieId','genres']]
rating_ = rating_2018_temp.groupby('movieId').mean()
rating_ = pd.merge(rating_, movie_temp, how='left', on = 'index')


# 2018年评分5分以上的电影及其对应的标签导出
rating_2018_good = rating_[rating_['rating'] >= 5]
rating_2018_good.to_csv('2018年评分5分以上的电影.csv')  


# 绘制电影复仇者联盟（The Avengers）每个月评分的平均值变化曲线图
rating_TheAvengers = rating[rating['movieId'] == 89745]
rating_TheAvengers.loc[:, 'timestamp'] = rating_TheAvengers['timestamp'].map(lambda x:
                                                                             time_start + datetime.timedelta(seconds=x))
rating_TheAvengers.loc[:, 'period'] = rating_TheAvengers['timestamp'].map(lambda x: x.to_period('M'))
rating_month = rating_TheAvengers.groupby('period')['rating'].mean()
plt.figure(figsize=(11, 8), dpi=120)
rating_month.plot(color='DarkBlue')
plt.xlabel('Month')
plt.ylabel('Rating')
plt.show()     