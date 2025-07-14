import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\machineLearning\lesson8-PCA\titanic.csv")

X = data[["Pclass","Sex","Age","Fare"]]
y = data["Survived"]

print(X.head())
print(X.info())


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

X["Sex"] = encoder.fit_transform(X["Sex"])

print(X.head())
print(X.info())

X["Age"].fillna(X["Age"].median(skipna=True), inplace= True)

print(X.head())
print(X.info())

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()

scaler.fit(X)
scaledData = scaler.transform(X)
print(scaledData)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)

pca.fit(scaledData)
newData = pca.transform(scaledData)

print(f"Pre PCA: {scaledData.shape}")
print(f"Post PCA: {newData.shape}")


# Display Scatter Plot
plt.figure(figsize=(5,5))
plt.scatter(newData[:,0],newData[:,1], c=y)

plt.xlabel("1st Principle Component")
plt.ylabel("2nd Principle Component")
plt.show()
