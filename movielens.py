# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:28:55 2020

@author: xiaobin
"""

'''
tag.csv 用户给电影打的标签:userId     用户id
                          movieId    电影id
                          tag        标签
                          timestamp  标记时间
rating.csv 用户给电影的评分:userId    用户id
                           movieId   电影id
                           rating    电影评分
                           timestamp 标记时间
movie.csv 电影信息:movieId   电影id
                   title     电影名
                   genres    电影类别
link.csv 链接到其他资源的id:movieId  电影id
                           imdbId   电影在imdb网站上的id
                           tmbdId   电影在themoviedb上的id
genome_scores.csv 电影和标签的相关性:movieId    电影id  
                                    tagId      标签id
                                    relevance  相关性
genome_tags.csv 包含标签的描述:tagId  标签id
                              tag    标签描述

读取rates.csv文件，完成：
将每1分做为一档，电影的评分共分为5档，(0:1], (1,2], (2, 3], (3, 4], (4, 5], 通过pandas包求出每个评分档共有多少部电影
添加一个comment列，对平均分4分以上的电影标‘推荐’，其他标‘不推荐’，输出到一个comment.csv中
'''
import pandas as pd

ratings = pd.read_csv('date/ml-latest-small/ratings.csv',index_col=None)
result = ratings.groupby(['rating']).size()

ratings['comment'] = ratings['rating'].apply(lambda x: '推荐' if x >= 4 else '不推荐')

ratings.to_csv('date/ml-latest-small/comment.csv', index = False)

ratings = pd.read_csv('date/ml-latest-small/comment.csv',index_col=None)

'''
对数据集中的3个csv文件进行聚合，生成一个csv，包含电影的信息，其中每部电影一行，信息包括电影名称、主演、平均分、所有tag
'''
import pandas as pd
import numpy as np

ratings = pd.read_csv('date/ml-latest-small/ratings.csv',index_col=None)
tags = pd.read_csv('date/ml-latest-small/tags.csv',index_col=None)
movies = pd.read_csv('date/ml-latest-small/movies.csv',index_col=None)


movies['rating_mean'] = ratings.groupby(['movieId'])['rating'].transform('mean') 

result = pd.merge(movies, tags, on = 'movieId', how = 'left')

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

