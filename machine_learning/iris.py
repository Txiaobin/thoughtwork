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

import pydot
import pydotplus
from sklearn import datasets
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO


X,y=datasets.load_iris(return_X_y=True)             #X与y
target_names=datasets.load_iris().target_names      #y的值列表:0:setosa,1:versicolor,2:virginica
feature_names=datasets.load_iris().feature_names    #特征X的名称列表

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

    
dot_data = StringIO()
tree.export_graphviz(mytree, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_dot('iris_simple.dot')
graph[0].write_png('iris_simple.png')


dot_data = tree.export_graphviz(clf,
                                out_file = None,
                                feature_names = iris.feature_names,
                                class_names = iris.target_names,
                                filled=True,
                                rounded=True
                               )
graph = pydotplus.graph_from_dot_data(dot_data)
display(Image(graph.create_png()))