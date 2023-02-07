import pandas as pd

df = pd.read_csv('netflix_titles.csv')
imdb_df = pd.read_csv('imdb_top_1000.csv')
#imdb_df = df.dropna()
df['cast'] = df['cast'].apply(lambda x : str(x))
df['cast'] = df['cast'].apply(lambda x : x.split(','))

#analyze how many new things per year
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year
grouped = df.groupby('year_added').count()
release_count = grouped['date_added']
release_count.to_csv('netflix_year_added.csv')

tv_df = df[df['type'] == 'TV Show']
movie_df = df[df['type'] == 'Movie']
tv_rel_grouped = tv_df.groupby('year_added').count()
tv_rel_count = tv_rel_grouped['date_added']
tv_rel_count.to_csv('TV_Count.csv')

movie_rel_grouped = movie_df.groupby('year_added').count()
movie_rel_count = movie_rel_grouped['date_added']
movie_rel_count.to_csv('Movie_count.csv')



#tv vs. movies by country
#see how average length of show has changed
#print(df['duration'].unique())

tv_df['duration'] = tv_df['duration'].apply(lambda x: int(x.split(' ')[0]))
#print(tv_df['duration'])
tv_grouped = tv_df.groupby('year_added')['duration'].mean()
tv_grouped.to_csv('tv_season_duration.csv')
#as netflix continues to strive for more content the quality of each goes down
#we are seeing more and more show with shorter seasons


#the movies added to netflix that are in the top 100
combined_df = pd.merge(df, imdb_df, left_on='title', right_on= 'Series_Title')
print(combined_df.info)

imdb_grouped = combined_df.groupby('year_added').count()
imdb_count = imdb_grouped['date_added']
print(imdb_count)
#movie_rel_count.to_csv('Movie_count.csv')
