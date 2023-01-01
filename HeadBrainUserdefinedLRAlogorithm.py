import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def HeadBrainUserLRA():
    Data = pd.read_csv('MarvellousHeadBrain.csv')

    print("Size of data set ",Data.shape)
    
    X = Data['Head Size(cm^3)'].values
    Y = Data['Brain Weight(grams)'].values

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    n = len(X)

    numerator = 0
    denometor = 0

    for i in range(n):
        numerator += (X[i] - mean_X)*(Y[i] - mean_Y)
        denometor += (X[i] - mean_X)**2

    m =numerator / denometor

    c = mean_Y - m * mean_X

    print("Slope of Regression Line :",m)
    print("Y intercept of Regression Line :",c)

    max_x = np.max(X)+100
    min_x = np.min(X)-100

    #Display plotting of above points

    x = np.linspace(min_x,max_x,n)

    y =c + m * x

    plt.plot(X,Y,color ='#58b970', label ='Regression Line')

    plt.scatter(X,Y, color = '#ef5423',label ='scatter Line')

    plt.xlabel('Head size in cm3')
    plt.ylabel('Brain weight in gram')
    plt.legend()
    plt.show()

    #Findout Goodness of fit i.e R Square

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m * X[i]
        ss_t += (Y[i] - mean_Y)**2
        ss_r += (Y[i] - y_pred)**2

    r2 = 1- (ss_r/ss_t)
    print(r2)




def main():
    print("Head Brain User defined Linear Alogithm..")

    HeadBrainUserLRA()

if __name__ == "__main__":
    main()