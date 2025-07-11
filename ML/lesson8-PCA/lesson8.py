import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
y = data["target"]
data = pd.DataFrame(data["data"],columns=data["feature_names"])

print(data.head())
print(data.info())

# Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaler.fit(data)
scaledData = scaler.transform(data)

print(scaledData)

# Preprocessing: PCA -> Principal Component Analysis
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

pca.fit(scaledData)
newData = pca.transform(scaledData)

print(f"Pre PCA: {scaledData.shape}")
print(f"Post PCA: {newData.shape}")


# Display Scatter Plot
plt.figure(figsize=(5,5))
plt.scatter(newData[:,0],newData[:,1], c=y)

plt.xlabel("1st Principal Component")
plt.ylabel("2nd Principal Component")
plt.show()