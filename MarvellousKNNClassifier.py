from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)
class MarvellousKNN():
    def fit(self,TraningData,TraningTarget):
        self.TraningData = TraningData
        self.TraningTarget = TraningTarget

    def predict(self,TestData):
        Predictions = []
        for row in TestData:
            lebel = self.closest(row)
            Predictions.append(lebel)
        return Predictions
    
    def closest(self,row):
        bestdistance = euc(row,self.TraningData[0])
        bestindex = 0
        for i in range(1,len(self.TraningData)):
            dist = euc(row,self.TraningData[i])
            if dist < bestdistance:
                bestdistance = dist
                bestindex = i
        return self.TraningTarget[bestindex]

def MarvellousKNeighbors():
    border = "_" * 70

    iris = load_iris()

    Data = iris.data
    Target = iris.target
    
    print(border)
    print("Actual Dataset ")
    print(border)

    for i in range(len(iris.target)):
        print("ID :%d ,Label :%s ,Features :%s"%(i,iris.data[i],iris.target[i]))
    print("Actual size of Dataset %d"%(i+1))

    Data_train,Data_test,Target_train,Target_test =train_test_split(Data ,Target ,test_size = 0.5)

    print(border)
    print("Traning Data set :")
    print(border)

    for i in range(len(Data_train)):
        print("ID: %d ,Label :%s ,Features :%s"%(i,Data_train[i],Target_train))
    print("Actual size of Traning Dataset %d"%(i+1))

    print(border)
    print("Testing Data set :")
    print(border)

    for i in range(len(Data_test)):
        print("ID: %d ,Label :%s ,Features :%s"%(i,Data_test[i],Target_test))
    print("Actual size of Testing Dataset %d"%(i+1))
    print(border)

    Classifer = MarvellousKNN()
    Classifer.fit(Data_train,Target_train)
    Predictions =Classifer.predict(Data_test)
    Accuracy = accuracy_score(Target_test,Predictions)

    return Accuracy



def main():
    Accuracy = MarvellousKNeighbors()
    print("Accuracy = ",Accuracy * 100,"%")

if __name__ == "__main__":
    main()