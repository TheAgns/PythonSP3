
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns  

data = pd.read_csv('../my_notebook/Mall_Customers.csv')


data.head(10) #printer  10 rows 


data.info() #Tjekker om der er nogle missing values i alle columns 

plt.plot(range(1,11), wcss)
plt.title('Kurve')
plt.xlabel('no of clusters')
plt.ylabel('wcss')
plt.show()


plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'rød', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blå', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'grøn', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clussters of cuustomers')
plt.xlabel('Annsual Income (k$)')
plt.ylabel('Spendding Score (1-100)')
plt.legend()
plt.show()