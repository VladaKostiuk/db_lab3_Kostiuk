import json
import psycopg2

username = 'postgres'
password = 'postgres'
database = 'lab2_Kostiuk'
host = 'localhost'
port = '5432'

TABLES = [
  'directors',
  'genres',
  'years',
  'films'
]


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)


data = {}
with conn:
    cur = conn.cursor()

    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]
        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows


with open('kostiuk_DB.json', 'w') as outf:
    json.dump(data, outf, default=str)
