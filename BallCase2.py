#Import requied library
from sklearn import tree

#load the dataset
#Rough :1
#Smooth :0

#Cricket :2
#Tennis : 1

Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

#Decide the Machine Learning Alogorithm
obj =tree.DecisionTreeClassifier()

#Perform the training of model
obj =obj.fit(Features, Labels)

#Perform the testing
print(obj.predict([[97,0],[35,1]]))
