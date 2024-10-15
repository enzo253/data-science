import numpy as np
import pandas as pd

df = pd.read_csv('Sprint_Projects/movies_2.csv')
print(df.head(5))

df["Rating"].fillna(value=df["Rating"].median(), inplace=True)

df["Rating"].fillna(value=df["Rating Count"].median(), inplace=True)

df["Genre"].fillna('', inplace=True)

print(df.describe().to_string(line_width=100))

print(df.columns)

df["Budget"].fillna(value=df["Budget"].median(), inplace=True)
df["Gross"].fillna(value=df["Gross"].median(), inplace=True)

df["Budget"] = df["Budget"].astype(int)

df["Gross"] = df["Gross"].astype(int)

df["Release Date"] = pd.to_datetime(df["Release Date"], errors='coerce')

filtered_movies = df[(df["Rating"] > 7) & (df["Gross"] > 50_000_000)]

filtered_movies = df[(df["Rating"] > 7) & (df["Gross"] > 50_000_000) & (df["MPAA Rating"].isin(["PG-13", 'G']))]

size_filter = df[(df["Genre"].str.contains("Animation") & (df["Rating"] > 7))]

animation_count = size_filter.shape[0]

top_5_budget = df.nlargest(5, "Budget")

top_budget_names = top_5_budget["Title"]

top_rated_comedys = df[df["Genre"].str.contains("Comedy")].nlargest(5, "Rating")

top_romance_date = df[(df["Genre"].str.contains("Romance")) & (df["Release Date"] > "1999-12-31")]

top_rated_romance = top_romance_date.nlargest(3, "Gross")
print(df.head(5))

top_5_expensive = df[(df["Budget"] & (df["Release Date"] > "1999-12-31"))]

top_budget = top_5_budget.nlargest(5, "Budget")

genre_counts = df["Genre"].value_counts()

average_budget_by_genre = df.groupby("Genre")["Budget"].mean()

most_favoured = df.groupby("Genre")["Rating"].mean()

top = most_favoured.nlargest(5)

highest_budget = average_budget_by_genre.idxmax(), average_budget_by_genre.max()

lowest_budget = average_budget_by_genre.idxmin(), average_budget_by_genre.min()

print(filtered_movies)
print(animation_count)
print(top_budget_names)
print(top_rated_comedys[['Title', 'Rating']])
print(top_rated_romance[['Title', 'Rating']])
print(genre_counts)
print(top_5_budget[['Title', 'Rating']])
print(f'\n{lowest_budget}{highest_budget}')
print(df.dtypes)
print(top)
print(df.tail(5))