import csv
import decimal
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'lab2_Kostiuk'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'products.csv'

query_0 = '''
CREATE TABLE films_new
(
  film_id SERIAL,
  film_name CHAR(50) NOT NULL,
  film_overview CHAR(1000) NOT NULL,
  CONSTRAINT pk_films_new PRIMARY KEY (film_id)
)
'''

query_1 = '''
DELETE FROM films_new
'''

query_2 = '''
INSERT INTO films_new (film_id, film_name, film_overview) VALUES (%s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:

    cur = conn.cursor()
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)

        for idx, row in enumerate(reader):
            values = (row['Film_ID'], row['Film_Name'], row['Film_Overview'])
            cur.execute(query_2, values)

    conn.commit()
