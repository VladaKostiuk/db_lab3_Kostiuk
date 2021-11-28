import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'postgres'
database = 'lab2_Kostiuk'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW YearlyReleasedFilms AS
select years.year_value, count(years.year_value) from 
films inner join years on films.year_id = years.year_id
group by years.year_value
'''

query_2 = '''
CREATE VIEW FilmGenresRatio AS
select genres.genre_name, count(genres.genre_name) 
from genres inner join films
on genres.genre_id = films.genre_id
group by genres.genre_name
'''

query_3 = '''
CREATE VIEW AmountOfEachDirectorFilms AS
select directors.director_name, count(directors.director_name) from 
films inner join directors on films.director_id = directors.director_id
group by directors.director_name
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute('DROP VIEW IF EXISTS YearlyReleasedFilms')

    cur.execute(query_1)

    cur.execute('SELECT * FROM YearlyReleasedFilms')

    data_to_visualise = {}

    for row in cur:
      data_to_visualise[row[0]] = row[1]

    x_range = range(len(data_to_visualise.keys()))
 
    figure, bar_ax = plt.subplots()
    bar = bar_ax.bar(x_range, data_to_visualise.values(), label='Total')
    bar_ax.set_title('Number of films that were released in a particular year')
    bar_ax.set_xlabel('Year')
    bar_ax.set_ylabel('Amount of films')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(data_to_visualise.keys())


    cur.execute('DROP VIEW IF EXISTS FilmGenresRatio')

    cur.execute(query_2)

    cur.execute('SELECT * FROM FilmGenresRatio')

    data_to_visualise = {}

    for row in cur:
      data_to_visualise[row[0]] = row[1]

    figure, pie_ax = plt.subplots()
    pie_ax.pie(data_to_visualise.values(), labels=data_to_visualise.keys(), autopct='%1.1f%%')
    pie_ax.set_title('Ratio of films of each genre in the database')


    cur.execute('DROP VIEW IF EXISTS AmountOfEachDirectorFilms')

    cur.execute(query_3)

    cur.execute('SELECT * FROM AmountOfEachDirectorFilms')

    data_to_visualise = {}

    for row in cur:
      data_to_visualise[row[0]] = row[1]

    x_range = range(len(data_to_visualise.keys()))
 
    figure, bar_ax = plt.subplots()
    bar = bar_ax.bar(x_range, data_to_visualise.values(), label='Total')
    bar_ax.set_title('Number of films made by each director')
    bar_ax.set_xlabel('Director name')
    bar_ax.set_ylabel('Amount of films')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(data_to_visualise.keys())


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()