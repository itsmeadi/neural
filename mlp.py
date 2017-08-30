from __future__ import division 
import numpy as np
from sklearn.datasets import make_classification
from sklearn.neural_network import MLPClassifier

X = [[0, 0], [1, 1]]
y = [0, 1]
clf = MLPClassifier(activation='tanh', learning_rate='constant',
 alpha=1e-4, hidden_layer_sizes=(15,), random_state=1, batch_size=1,verbose= True,
 max_iter=1, warm_start=True)
clf.fit(X, y)   
a=clf.predict([[2., 2.], [-1., -2.]])
print a
X = [[2, 2], [3, 3]]
y = [2, 3]

clf.partial_fit(X,y)
a=clf.predict([[1,1], [2,2]])

print a
