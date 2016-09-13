import sqlite3

db = sqlite3.connect('database.db')
#db.execute('insert into person(firstname, secondname, age) values("Alex", "Bowers", 17)')

db.execute('update person set firstname = "AlexAss" where secondname = "Bowers"')

db.commit()