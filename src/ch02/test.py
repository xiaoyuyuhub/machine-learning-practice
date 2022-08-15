import KNN

datd,datl=KNN.file2matrix('datingTestSet.txt')

group, labels = KNN.createDataSet();
KNN.classify0([3, 3], group, labels, 3);
