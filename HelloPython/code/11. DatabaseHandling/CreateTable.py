import sqlite3

db = sqlite3.connect('database.db')

db.execute('drop table if exists person')
db.execute('create table person(firstname text,secondname text, age int)')

db.execute('drop table if exists animal')
db.execute('create table animal(name text, age int)')

