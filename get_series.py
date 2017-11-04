from imdbpie import Imdb
import pandas as pd
from halo import Halo

imdb = Imdb(anonymize=True)

series = imdb.popular_shows()

cols = ["Title", "Actors", "Genres", "Rating", "Running Time", "Year", "Certification", "Writers"]

df = pd.DataFrame(columns=cols)

spinner = Halo(text='Loading', spinner='dots')

spinner.start()

for j, el in enumerate(series):
	show = imdb.get_title_by_id(el["tconst"])
	title = show.title
	actors = ', '.join(i["name"] for i in el["principals"])
	genres = ', '.join(i for i in show.genres)
	genres = ', '.join(i for i in show.genres)
	rating = show.rating
	rtime = show.runtime
	year = show.year
	cert = show.certification
	writers = ', '.join(i.name for i in show.writers_summary)
	spinner.text = "Running - " + str((j+1)/0.5) + "%"
	df.loc[j] = [title, actors, genres, rating, rtime, year, cert, writers]

df.to_csv("shows.csv")
spinner.stop()