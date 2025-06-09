# Linear Regression

X = [1,2,3,4,5]
Y = [1,3,2,3,5]

def findMean(inList):
    return sum(inList)/len(inList)

meanX = findMean(X)
meanY = findMean(Y)

print(f"Mean X: {meanX} \nMean Y: {meanY}")

#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)

num = 0
den = 0

for i in range(len(X)):
    num += ((X[i] - meanX)*(Y[i] - meanY))
    den += pow((X[i]-meanX),2)

m = round(num/den,1)

#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)
# c = mean(y) - m * mean(x)
c= round(meanY - m * meanX,1)

print(f"Manual Method:\n    m = {m}\n    c = {c}")

# Machine Learning
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([[1],[3],[2],[3],[5]])

Reg = LinearRegression()

Reg = Reg.fit(X,Y)

print(f"ML Method:\n    m = {Reg.coef_}\n    c = {Reg.intercept_}")




#m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)
# c = mean(y) - m * mean(x)

x2 = np.array([[1],[2],[3],[4],[5]])
y2 = np.array([[2],[4],[6],[8],[10]])

Reg2 = LinearRegression()

Reg2.fit(x2,y2)

print(f"ML Method:\n    m = {Reg2.coef_}\n    c = {Reg2.intercept_}")