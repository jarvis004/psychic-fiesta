from imdbpie import Imdb
import pandas as pd
from halo import Halo

imdb = Imdb(anonymize=True)

movies = imdb.top_250()

cols = ["Title", "Actors", "Director", "Genres", "Rating", "Running Time", "Year", "Certification", "Writers"]
df = pd.DataFrame(columns=cols)

spinner = Halo(text='Loading', spinner='dots')

spinner.start()

for j, el in enumerate(movies):
	movie = imdb.get_title_by_id(el["tconst"])
	title = movie.title
	actors = ', '.join(i.name for i in movie.cast_summary)
	director = movie.directors_summary[0].name
	genres = ', '.join(i for i in movie.genres)
	rating = movie.rating
	rtime = movie.runtime
	year = movie.year
	cert = movie.certification
	writers = ', '.join(i.name for i in movie.writers_summary)
	spinner.text = "Running - " + str((j+1)/2.5) + "%"
	df.loc[j] = [title, actors, director, genres, rating, rtime, year, cert, writers]

df.to_csv("movies.csv")
spinner.stop()