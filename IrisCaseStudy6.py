# User created KNN Library
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier

def MarvellousCalculateAccuracyDecisionTree():
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_train,Data_test,Target_train,Target_test = train_test_split(Data ,Target,test_size =0.5)

    Classifer = DecisionTreeClassifier()

    Classifer.fit(Data_train ,Target_train)
    Predictions = Classifer.predict(Data_test)

    Accuracy =accuracy_score(Target_test ,Predictions)

    return Accuracy

def MarvellousCalculateAccuracyKNeighbor():
    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    Data_train,Data_test,Target_train,Target_test = train_test_split(Data ,Target,test_size =0.5)

    Classifer = KNeighborsClassifier()

    Classifer.fit(Data_train ,Target_train)
    Predictions = Classifer.predict(Data_test)

    Accuracy =accuracy_score(Target_test ,Predictions)

    return Accuracy

def main():
    Accuracy = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of classification algorithm with Decision Tree Classifer is :",Accuracy*100,"%")

    Accuracy = MarvellousCalculateAccuracyKNeighbor()
    print("Accuracy of classification algorithm with KNN Classifer is :",Accuracy*100,"%")

if __name__ =="__main__":
    main()
