import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import  train_test_split
import schedule
import time
import datetime
import os
import time
from sys import *

def BallKNN(log_dir = "Marvellous" ):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator ="_" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log"%(time.ctime()))
    f = open(log_path,'w')
    f.write(separator +"\n")
    f.write("Ball Case Study Accuracy :"+time.ctime()+"\n")
    f.write(separator + "\n")

    df = pd.DataFrame({'weight':[35,47,90,48,90,35,92,35,35,35,96,43,110,35,95],'Pattern':['Rough','Rough','Smooth','Rough','Smooth','Rough','Smooth','Rough','Rough','Rough','Smooth','Rough','Smooth','Rough','Smooth'],'Label':["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]})
    df.to_csv('Ball.csv',index =False)

    Data = pd.read_csv('Ball.csv')

    print("Size of Data :",Data.shape)
    print("first 4 Records :\n",Data.head(4))
    print("Last 3 Records :\n",Data.tail(3))


    Weight = Data.weight
    Pattern = Data.Pattern
    Label = Data.Label

    le =preprocessing.LabelEncoder()
    Weight_encoded = le.fit_transform(Weight)
    print(Weight_encoded)
    Patter_encoded = le.fit_transform(Pattern)
    print(Patter_encoded)
    Label_encoded = le.fit_transform(Label)
    print(Label_encoded)

    features =list(zip(Weight_encoded,Patter_encoded))
    Data_train,Data_test,Target_train,Target_test = train_test_split(features ,Label,test_size =0.5)

    Classifer = DecisionTreeClassifier()

    Classifer.fit(Data_train ,Target_train)

    Predictions = Classifer.predict(Data_test)

    Accuracy =accuracy_score(Target_test ,Predictions)

    f.write("%d\n" % (Accuracy *100))

    X = Data['weight'].values
    Y = Data['Pattern'].values

    plt.plot(X,Y,color ='#58b970', label ='Ball Line')
    plt.scatter(X,Y, color = '#ef5423',label ='scatter Line')

    plt.xlabel('weight')
    plt.ylabel('Pattern')
    plt.legend()

    plt.show()
    plt.savefig('foo.png',bbox_inches='tight',facecolor='auto')
    #plt.savefig('foo.pdf')
    


def main():
    print("____Ball Case Study---------")
    print("Automation script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : this script is used to perform ------")
        exit()

    if((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ___number of argument as")
        print("First Argument as :______")
        print("Second Argument as :______")
        exit()
    try:
        BallKNN(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception:
        print("Error : Invalid input")

    schedule.every(2).minutes.do(BallKNN)
    
    while(1):
        schedule.run_pending()
        time.sleep(1)



if __name__=="__main__":
    main()