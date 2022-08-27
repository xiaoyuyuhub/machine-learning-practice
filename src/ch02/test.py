import KNN

datd,datl=KNN.file2matrix('datingTestSet.txt')

group, labels = KNN.createDataSet();
KNN.classify0([0.2, 0.6], group, labels, 3);
