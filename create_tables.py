import sqlite3

connexion = sqlite3.connect('data.db')
cursor = connexion.cursor()
#Création d'une table
create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)'
cursor.execute(create_table)

create_table = 'CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, msg text, user text)'
cursor.execute(create_table)

connexion.commit()
connexion.close()