import numpy as np
from sklearn import linear_model
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
Y = np.array([1, 1, 2, 2])
clf = linear_model.SGDClassifier()
clf.partial_fit(X, Y,classes=np.unique(Y))

print(clf.predict([[-0.8, -1]]))

X = np.array([-0.8, -1])
Y = np.array([2])
X=X.reshape(1, -1)
clf.partial_fit(X, Y)
print(clf.predict([[-0.8, -1]]))
