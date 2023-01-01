from sklearn.datasets import load_iris

iris =load_iris()

print("Features names of iris data set ")
print(iris.feature_names)

print("Target names of iris data set")
print(iris.target_names)

print("element from iris data set")

for i in range(len(iris.target)):
    print("ID: %d ,Label: %s ,Features : %s"%(i,iris.data[i],iris.target[i]))