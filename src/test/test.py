import KNN

group, labels=KNN.createDataSet()
print(KNN.classify0([3,3],group,labels,3))