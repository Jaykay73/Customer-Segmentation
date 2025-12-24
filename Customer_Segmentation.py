import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


file_path = 'Mall_Customers.csv'
data = pd.read_csv(file_path)

features = data[['Annual Income (k$)', 'Spending Score (1-100)']]

kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(features)

plt.figure(figsize=(10, 6))

for cluster in range(5):
    cluster_data = features[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Annual Income (k$)'], cluster_data['Spending Score (1-100)'], label=f'Cluster {cluster}')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s=300, c='black', marker='X', label='Centroids')

plt.title('Customer Segments Based on Purchasing Behavior')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
