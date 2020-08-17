# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 17:24:27 2020

@author: xiaobin
"""

'''
通过花的属性数据预测花的种类,尝试构建决策树模型,要求最大树深度为3
尝试预测sepal length=6,sepal width=1,petal length=3,petal width=1最可能是什么类型的花
可视化决策树,解释下什么样的花最可能是setosa
'''

import pydotplus
from IPython.display import Image, display
from sklearn import datasets
from sklearn import tree
from sklearn.cross_validation import train_test_split

iris = datasets.load_iris()
X=iris['data']
y=iris['target']

X_train,X_test,Y_train,Y_test = train_test_split(X,y,test_size=0.25,random_state=1)
mytree = tree.DecisionTreeClassifier(max_depth=3)
mytree.fit(X_train,Y_train)

sum = 0
predict = mytree.predict(X_test)
for i in range(len(Y_test)):
    if predict[i]==Y_test[i]:
        sum +=1
print("预测率：%s"%(sum/len(Y_test)))

print("sepallength=6,sepalwidth=1,petallength=3,petalwidth=1最可能是",target_names[mytree.predict([[6,1,3,1]])[0]])

dot_data = tree.export_graphviz(mytree,
                                out_file = None,
                                feature_names = iris['feature_names'],
                                class_names = iris['target_names'],
                                filled=True,
                                rounded=True
                               )
graph = pydotplus.graph_from_dot_data(dot_data)
display(Image(graph.create_png()))


'''
可以看出，花瓣短窄的花最可能是setosa。
'''