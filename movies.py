import sqlite3

# Connect to the database (new/existing)
db = sqlite3.connect('mydb.db')
cursor = db.cursor()

movies = [
    {'title': 'RRR', 'year': 2022, 'director': 'SS rajamouli', 'actor': 'ram charan', 'actress': 'alia bhatt'},
    {'title': 'kick', 'year': 2016, 'director': 'sajid nadidawala', 'actor': 'salman khan', 'actress': 'jacquiline'},
    {'title': 'bajrangi', 'year': 2018, 'director': 'kabir khan', 'actor': 'salman khan', 'actress': 'kareena kapoor'},
    {'title': '3-idiot', 'year': 2011, 'director': 'raju irani', 'actor': 'amir khan', 'actress': 'kareena kapoor'},
    {'title': 'The Dark Knight', 'year': 2008, 'director': 'Christopher Nolan', 'actor': 'Christian Bale', 'actress': 'Heath Ledger'},
    {'title': 'Avengers:infinity', 'year': 2018, 'director': 'Anthony Russo', 'actor': 'Robert Downey Jr', 'actress': 'Chrissie Smith'},
    {'title': 'race 1', 'year': 2013, 'director': 'remo d souza', 'actor': 'saif ali khan', 'actress': 'jaquline'}
]

# Creating table 'Movies'
cursor.execute("CREATE TABLE Movies8 (title VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director VARCHAR(24));")

# Inserting data into the table
for movie in movies:
    cursor.execute(f"INSERT INTO Movies8 VALUES (\'{movie['title']}\', \'{movie['actor']}\', \'{movie['actress']}\', {movie['year']}, \'{movie['director']}\');")

# Select all movies
print("\nSelect all movies:")
cursor.execute("SELECT * FROM Movies8;")
for i in cursor.fetchall():
    print(i)
print("\n")

# Select all movies with the actor 'Robert Downey Jr'
print("Select all movies with the actor 'Robert Downey Jr':")
cursor.execute("SELECT title, year, director FROM Movies8 WHERE actor='Robert Downey Jr';")
for i in cursor.fetchall():
    print(i)
print("\n")


# Printing the table in a dataframe
# import pandas as pd
# print(pd.read_sql("SELECT * FROM Movies8;", db),end="\n\n")
# print(pd.read_sql("SELECT title, year, director FROM Movies8 WHERE actor='Robert Downey Jr';", db))
