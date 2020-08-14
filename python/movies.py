import pandas as pd
import time

tags = pd.read_csv('ml-25m/tags.csv')
ratings = pd.read_csv('ml-25m/ratings.csv')
movies = pd.read_csv('ml-25m/movies.csv')
links = pd.read_csv('ml-25m/links.csv')


# 1. 不同用户
users = list()
users.extend(tags['userId'].tolist())
users.extend(ratings['userId'].tolist())


# 2. 不同电影
m = movies['movieId'].tolist()

# 3. 不同电影种类
m_type_tmp = movies['genres'].tolist()
m_type = list()
for item in m_type_tmp:
    if '|' in item:
        m_type.extend(item.split('|'))
    else:
        m_type.append(item)

# 4. 电影无外部链接
all_movie_id = set(movies['movieId'].tolist())
has_link_movie_id = set(links['movieId'].tolist())
no_link_movie_id = all_movie_id - has_link_movie_id

# 2018年进行电影评分用户
def trans(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y", time_local)
    return dt

ratings['timestamp'] = ratings['timestamp'].apply(trans)
ratings_t_2018 = ratings[ratings['timestamp'] == '2018']
u = ratings_t_2018['userId'].tolist()



print('1. 一共有 %s 不同的用户' % (str(len(set(users)))))
print('2. 一共有 %s 不同的电影' % (str(len(set(m)))))
print('3. 一共有 %s 不同的电影种类' % (str(len(set(m_type)))))
print('4. 一共有 %s 电影没有外部链接' % (str(len(no_link_movie_id))))
print('5. 2018年一共有 %s 人进行电影评分' % (str(len(set(u)))))
