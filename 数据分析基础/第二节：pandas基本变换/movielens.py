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
                              
对数据集中的3个csv文件进行聚合，生成一个csv，包含电影的信息，其中每部电影一行，信息包括电影名称、主演、平均分、所有tag
'''
import pandas as pd
import numpy as np

ratings = pd.read_csv('ml-latest-small/ratings.csv',index_col=None)
tags = pd.read_csv('ml-latest-small/tags.csv',index_col=None)
movies = pd.read_csv('ml-latest-small/movies.csv',index_col=None)


movies['rating_mean'] = ratings.groupby(['movieId'])['rating'].transform('mean') 

result = pd.merge(movies, tags, on = 'movieId', how = 'left')