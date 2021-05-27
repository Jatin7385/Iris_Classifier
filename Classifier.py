#Loading required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
#Loading Datasets
iris=datasets.load_iris()

#Printing description and features
#print(iris.DESCR)
features = iris.data
labels = iris.target

#Training the classifier.
clf = KNeighborsClassifier()
clf.fit(features ,labels)

preds = clf.predict([[31,1,1,1]])
print(preds)