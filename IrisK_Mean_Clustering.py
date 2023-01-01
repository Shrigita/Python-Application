import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans

def iriskmean():
    dataset = pd.read_csv("iris.csv")
    x = dataset.iloc[:,[0,1,2,3]].values

    wcss =[]

    for i in range (1,11):
        kmeans = KMeans(n_clusters = i,init = 'k-means++',max_iter = 300,n_init = 10,random_state = 0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)

    #Ploatting the result onto a line graph ,allowing us to observe  'the elbow'
    plt.plot (range(1,11),wcss)
    plt.title('The elbow method')
    plt.xlabel('Number of cluster')
    plt.ylabel('WCSS')  #with cluster sum of squares
    plt.show()

    #Applying Kmeans to the dataset /Creating the Kmean classifier
    kmeans = KMeans(n_clusters = 3,init = 'k-means++',max_iter = 300,n_init = 10,random_state = 0)
    y_kmeans =kmeans.fit_predict(x)

    #visualising the cluster
    plt.scatter(x[y_kmeans == 0,0],x[y_kmeans == 0,1],s = 100 ,c ='red',label = 'Iris-setosa')
    
    plt.scatter(x[y_kmeans == 1,0],x[y_kmeans == 1,1],s = 100 ,c ='blue',label = 'Iris-versicolour')

    plt.scatter(x[y_kmeans == 2,0],x[y_kmeans == 2,1],s = 100 ,c ='green',label = 'Iris-virginica')

    #plotting the centeroid of the cluster
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s =100,c ='yellow',label ='Centroid')

    plt.legend()

    plt.show()


def main():
    print("Unsupervised Machine Learning")

    print("K Mean Clustering Algorithm")

    iriskmean()

if __name__ == "__main__":
    main()