import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

df.columns = df.columns.str.strip()

print(df.head())
print(df.describe())

type_count = df["type"].value_counts()
plt.pie(type_count, labels=type_count.index, autopct='%1.1f%%')
plt.title("Movies vs TV Shows Distribution")
plt.show()

top_countries = df["country"].value_counts().head(5)
top_countries.plot(kind="bar")
plt.title("Top 5 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

release_trend = df["release_year"].value_counts().sort_index()
release_trend.plot()
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Releases")
plt.show()
