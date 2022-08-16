import trees

myDat, labels = trees.create_dataset()
print(myDat)

print(trees.choose_best(myDat))