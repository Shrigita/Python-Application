import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

    #1 .Load Data
    data =pd.read_csv(data_path,index_col = 0)
    print("Size Of Actual Dataset ",len(data))

    #2 .Clean ,Prepare and Manipulate the Data
    features_name = ['Whether','Temperature']
    print("Name of Features :",features_name)

    Whether = data.Whether
    Temperature = data.Temperature
    Play = data.Play
    #Creating Label Encoding
    le =preprocessing.LabelEncoder()

    #Convert String Label into Number
    whether_encoded = le.fit_transform(Whether)
    print(whether_encoded)

    temp_encoded = le.fit_transform(Temperature)
    print(temp_encoded)

    label =le.fit_transform(Play)
    print(label)

    #Combine Whether and Temperature into single list of tuples
    features = list(zip(whether_encoded,temp_encoded))

    # 3.Train Data
    model = KNeighborsClassifier(n_neighbors = 3)

    model.fit(features ,label)

    #4. Test data
    Prediction = model.predict([[0,2],])
    print(Prediction)


def main():
    print("Machine Learning Application")
    print("Play Prediction Appliction using K Nereast Knighbor Algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ =="__main__":
    main()
