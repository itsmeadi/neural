from sklearn.feature_extraction.text import HashingVectorizer
import numpy as np
from sklearn.naive_bayes import MultinomialNB

# Training with first training set
targets = ['education','film','sports','laptops','phones']
x = ["football is the sport","gravity is the movie", "education is imporatant","lenovo is a laptop","android phones"]
y = np.array([2,1,0,3,4])
clf = MultinomialNB()
vectorizer = HashingVectorizer(stop_words='english', non_negative=True,
                                   n_features=32*2)
print vectorizer
X_train = vectorizer.transform(x)
print X_train
clf.partial_fit(X_train, y, classes=[0,1,2,3,4])

#Testing with First training set
test_data = ["android","lenovo","Transformers"]
X_test = vectorizer.transform(test_data)
print "Using Initial classifier"
pred = clf.predict(X_test)
for doc, category in zip(test_data, pred):
    print('%r => %s' % (doc, targets[category]))

# Training with updated training set
x = ["cricket", "Transformers is a film","which college"]
y = np.array([2,1,0])
X_train = vectorizer.transform(x)
clf.partial_fit(X_train, y)

# Testing with the updated trainign set
test_data = ["android","lenovo","Transformers"]
X_test = vectorizer.transform(test_data)
print "\nUsing Updatable classifiers"
pred = clf.predict(X_test)
for doc, category in zip(test_data, pred):
    print('%r => %s' % (doc, targets[category]))