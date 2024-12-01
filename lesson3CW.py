# pandas
# intro to pandas - 1
import pandas as pd
# create a dataframe
data = {
    "Name" : ["Alice","Bob","Charlie"],
    "Age" : [25,30,35],
    "City" : ["New York", "San Francisco", "Ohio"]
}

df  = pd.DataFrame(data)
# display the data and other basic info
print(df.head())

data1 = [{"Name" : "Alice", "Age" : 25, "City":"New York"}, {"Name" : "Bob", "Age" : 30, "City":"Los Angeles"}]

df1 = pd.DataFrame(data1)
print(df1.head())

# shape: returns the number of rows and columns in the data frame
print(df.shape)
print(df["Name"])