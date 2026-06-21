# Customer Segmentation with K-Means Clustering

## Project Overview

This project applies the K-Means Clustering algorithm to group mall customers into distinct segments based on their Annual Income and Spending Score.

Customer segmentation helps businesses understand purchasing behavior, identify valuable customer groups, and create targeted marketing strategies.

---

## Objective

The primary goal of this project is to:

- Analyze customer spending patterns.
- Discover hidden customer groups.
- Visualize customer segments using clustering.
- Determine the optimal number of clusters using the Elbow Method.

---

## Dataset Information

The dataset contains customer information collected from a shopping mall.

### Features Used

1. Annual Income (k$) – Customer's yearly income.
2. Spending Score (1-100) – Score assigned based on customer spending behavior.

These two features were selected to identify customers with similar purchasing habits.

---

## Methodology

### 1. Data Preparation

- Imported the dataset using Pandas.
- Selected relevant features.
- Checked for missing values.
- Prepared data for clustering.

### 2. Finding the Optimal Number of Clusters

The Elbow Method was used to determine the best value of K.

For each value of K (1–10), the Within Cluster Sum of Squares (WCSS) was calculated.

The graph showed that the curve begins to flatten around K = 5, indicating the optimal number of clusters.

### Elbow Method Result

- Optimal Clusters: 5
- Evaluation Metric: WCSS (Within Cluster Sum of Squares)

### 3. K-Means Clustering

After selecting K = 5:

- K-Means algorithm was trained.
- Customers were assigned to clusters.
- Cluster centroids were calculated automatically.
- Results were visualized using a scatter plot.

---

## Cluster Analysis

The model identified five distinct customer groups:

### Cluster 1
- Medium Income
- Medium Spending Score

### Cluster 2
- High Income
- High Spending Score
- Premium Customers

### Cluster 3
- Low Income
- High Spending Score
- Frequent Shoppers

### Cluster 4
- High Income
- Low Spending Score
- Conservative Spenders

### Cluster 5
- Low Income
- Low Spending Score
- Budget-Conscious Customers

---

## Visualization

### Elbow Method

Used to identify the optimal number of clusters before training the model.

## Elbow Method Graph

![Elbow Method](elbow_method.png)



### Customer Segmentation Plot

The scatter plot displays:

- Different colors representing different customer groups.
- Yellow markers representing cluster centroids.
- Clear separation between customer categories.



## Customer Segmentation Result

![Customer Segmentation](customer_segmentation_map.png) 

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## How to Run

Install Required Libraries:

pip install pandas numpy matplotlib scikit-learn

Run the Program:

main.py



---

## Project Workflow

Dataset
↓
Data Preprocessing
↓
Feature Selection
↓
Elbow Method
↓
Optimal K Selection
↓
K-Means Clustering
↓
Visualization
↓
Customer Insights

---

## Outcome

This project successfully segmented customers into five meaningful groups using K-Means Clustering. The resulting clusters provide valuable insights into customer behavior and can assist businesses in making data-driven marketing and customer engagement decisions.

---

Internship Task

Prodigy InfoTech – Machine Learning Internship

Task 02: Create a K-Means clustering model to group customers based on their purchasing behavior and spending patterns.
