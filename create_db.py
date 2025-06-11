import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

INSERT_CLIENT_SQL = "INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)"

clients = [
    ('DUPONT', 'Emilie', '123, Rue des Lilas, 75001 Paris'),
    ('LEROUX', 'Lucas', '456, Avenue du Soleil, 31000 Toulouse'),
    ('MARTIN', 'Amandine', '789, Rue des Érables, 69002 Lyon'),
    ('TREMBLAY', 'Antoine', '1010, Boulevard de la Mer, 13008 Marseille'),
    ('LAMBERT', 'Sarah', '222, Avenue de la Liberté, 59000 Lille'),
    ('GAGNON', 'Nicolas', '456, Boulevard des Cerisiers, 69003 Lyon'),
    ('DUBOIS', 'Charlotte', '789, Rue des Roses, 13005 Marseille'),
    ('LEFEVRE', 'Thomas', '333, Rue de la Paix, 75002 Paris')
]

for client in clients:
    cur.execute(INSERT_CLIENT_SQL, client)

connection.commit()
connection.close()
