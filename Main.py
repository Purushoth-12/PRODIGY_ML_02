# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load Dataset
df = pd.read_csv("Mall_Customers.csv")

# Display Dataset Information
print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

# Select Features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow Method
plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('elbow_method.png')
plt.show()

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Plot Customer Segments
plt.figure(figsize=(10,7))

plt.scatter(X.iloc[y_kmeans == 0, 0],
            X.iloc[y_kmeans == 0, 1],
            s=100, c='red', label='Cluster 1')

plt.scatter(X.iloc[y_kmeans == 1, 0],
            X.iloc[y_kmeans == 1, 1],
            s=100, c='blue', label='Cluster 2')

plt.scatter(X.iloc[y_kmeans == 2, 0],
            X.iloc[y_kmeans == 2, 1],
            s=100, c='green', label='Cluster 3')

plt.scatter(X.iloc[y_kmeans == 3, 0],
            X.iloc[y_kmeans == 3, 1],
            s=100, c='cyan', label='Cluster 4')

plt.scatter(X.iloc[y_kmeans == 4, 0],
            X.iloc[y_kmeans == 4, 1],
            s=100, c='magenta', label='Cluster 5')

# Plot Centroids
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=300,
            c='yellow',
            marker='X',
            label='Centroids')

plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.savefig('customer_clusters.png')
plt.show()

print("\nCustomer Segmentation Completed Successfully!")
