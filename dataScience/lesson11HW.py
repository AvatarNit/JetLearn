import numpy as np
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv(r"C:\Users\sajja\OneDrive\Desktop\VSCode\dataScience\lesson11-income\avatar.csv")

data = data[["book_num", "chapter_num", "imdb_rating"]]

print(data.describe())
print(data.info())

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
data["imdb_rating"] = imputer.fit_transform(data[["imdb_rating"]]).ravel()

print("After Imputing:\n", data[["imdb_rating"]])


avgRatings = data.groupby("book_num")["imdb_rating"].mean()
fig1 = go.Figure()

fig1.add_trace(go.Bar(x=avgRatings.index, y=avgRatings.values, marker_color='orange'))
fig1.update_layout(
    title="Average IMDB Rating per Book",
    xaxis_title="Book Number",
    yaxis_title="Average IMDB Rating"
)

fig1.write_html("fig1.html",auto_open=True)


fig2 = go.Figure()
book1Data = data[data["book_num"] == 1]
avgRatingsEp = book1Data.groupby("chapter_num")["imdb_rating"].mean()
fig2.add_trace(go.Scatter(x=avgRatingsEp.index, y=avgRatingsEp.values, fill="tonexty", line_color="deepskyblue"))
fig2.update_layout(
    title="IMDB Rating per Episode in Book 1",
    xaxis_title="Episode Number",
    yaxis_title="IMDB Rating"
)
fig2.write_html("fig2.html",auto_open=True)


fig3 = go.Figure()
book2Data = data[data["book_num"] == 2]
avgRatingsEp = book2Data.groupby("chapter_num")["imdb_rating"].mean()
fig3.add_trace(go.Scatter(x=avgRatingsEp.index, y=avgRatingsEp.values, fill="tonexty", line_color="forestgreen"))
fig3.update_layout(
    title="IMDB Rating per Episode in Book 2",
    xaxis_title="Episode Number",
    yaxis_title="IMDB Rating"
)
fig3.write_html("fig3.html",auto_open=True)


fig4 = go.Figure()
book3Data = data = data[data["book_num"] == 3]
avgRatingsEp = data.groupby("chapter_num")["imdb_rating"].mean()
fig4.add_trace(go.Scatter(x=avgRatingsEp.index, y=avgRatingsEp.values, fill="tonexty", line_color="crimson"))
fig4.update_layout(
    title="IMDB Rating per Episode in Book 3",
    xaxis_title="Episode Number",
    yaxis_title="IMDB Rating"
)
fig4.write_html("fig4.html",auto_open=True)
