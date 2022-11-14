import logRegres
from numpy.ma import array

data_matrix, label_matrix=logRegres.load_data_set()


wi=logRegres.grad_ascent(data_matrix,label_matrix)

logRegres.plot_best_fit(weights.getA())
