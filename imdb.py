import pandas as pd

df = pd.read_csv('imdb_top_1000.csv')
df = df.dropna()
print(df.dtypes)

#best directors by ratings
director_ratings = df.groupby('Director')['IMDB_Rating'].mean()
director_ratings = director_ratings.sort_values(ascending = False)
top_20 = director_ratings.iloc[:20]
top_20.to_csv('imdb_director_ratings.csv')

director_meta = df.groupby('Director')['Meta_score'].mean()
director_meta = director_meta.sort_values(ascending = False)
top_20_meta = director_meta.iloc[:20]

df['Gross'] = df["Gross"].str.replace(',','').astype(int)
director_gross = df.groupby('Director')['Gross'].mean()
director_gross =director_gross.sort_values(ascending=False)
director_gross.iloc[:20].to_csv('top_grossing_directors.csv')

#print(top_20_meta)
#top_20.to_csv('imdb_director_ratings.csv')

#what stars lead to gross

star_df = df.groupby('Star1')['Gross'].mean()
star_df = star_df.sort_values(ascending = False)
#print(star_df.iloc[:20])
#highest grossing actors
star_df.iloc[:20].to_csv('top_grossing_stars.csv')








#print(director_ratings.iloc[:20])