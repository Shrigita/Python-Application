from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    #Load Dataset
    wine =datasets.load_wine()

    #print name of features
    print(wine.feature_names)

    #print name of label species(class_0,class_1,class_2)
    print(wine.target_names)

    #print the wine data (top 6 records)
    print(wine.data[0:6])

    #print the wine label(class_0,class_1,class_2)
    print(wine.target)

    #split dataset into training set and test set
    X_train,X_test,Y_train,Y_test = train_test_split(wine.data,wine.target,test_size = 0.3)

    #create KNN Classifier object
    knn = KNeighborsClassifier(n_neighbors =3)

    #train the model
    knn.fit(X_train,Y_train)

    #test the model
    Y_pred =knn.predict(X_test)

    #Model  Accuracy,how often is the classifier correct?
    print("Accuracy", metrics.accuracy_score(Y_test,Y_pred))







def main():
    print("Machine Learning Application")

    print("Wine Predictor Application using K Nearest Knighbor Algorithm")

    WinePredictor()

if __name__ =="__main__":
    main()