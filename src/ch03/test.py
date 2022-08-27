import trees
import treePlotter

myDat, labels = trees.create_dataset()
print(myDat)

# tree=trees.create_tree(myDat,labels)

print(treePlotter.retrieve_tree(1))

tree=treePlotter.retrieve_tree(0)

treePlotter.create_plot(tree)

print(trees.classify(tree,labels,[1,1]))