import matplotlib.pyplot as plt

# Histogram - ranges of values grouped together to make bars
ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages,bins,histtype="bar", rwidth=0.8)
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

# Scatter Plot
x = [1,2,3,4,5,6,7,8,9]
y = [0,1,0,1,0,1,0,1,0]

plt.scatter(x,y, color="orange",marker="o",s=50)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Scatter Plot")
plt.show()

# Pie chart
activities = ["Sleep","Study","TV","Eating","Procrastinating"]
hours = [9,2,4,3,6]
clr = ["g","m","r","b","y"]

plt.pie(hours,labels=activities,colors=clr,startangle=90,shadow=True)
plt.title("Day Chart")
plt.show()

# Stack Plot
days = [1,2,3,4,5]

sleep = [7,8,6,8,10]
study = [2,1,3,2,0]
tv = [2,4,3,4,6]
eating = [2,3,3,1,3]
procrastinating = [11,8,9,9,5]

# Making plots for legend with colors
plt.plot([],[], color="g",label="Sleep",linewidth=5)
plt.plot([],[], color="m",label="Study",linewidth=5)
plt.plot([],[], color="r",label="TV",linewidth=5)
plt.plot([],[], color="b",label="Eating",linewidth=5)
plt.plot([],[], color="y",label="Procrastinating",linewidth=5)
# Colors should match ^ v
plt.stackplot(days,sleep,study,tv,eating,procrastinating, colors = clr)
plt.xlabel("Days")
plt.ylabel("Activities")
plt.title("Stack plot")
plt.legend()
plt.show()


import numpy as np

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

t1 = np.arange(0,5,0.1)
# divides screen into grid to display different plots
plt.figure()
# This would make it 2x2 and put this plot at position 1
plt.subplot(221)
plt.plot(t1,f(t1),"bo")

# Cosine graph
def f1(t):
    return np.cos(2*np.pi*t)

t2 = np.arange(0,5,0.02)
# This would make it 2x2 and put this plot at position 4
plt.subplot(224)
plt.plot(t2,f1(t2),"ro")

plt.show()

