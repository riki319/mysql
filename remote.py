import MySQLdb

from config import data

db = MySQLdb.connect(**data)

cur = db.cursor()


cur.execute("SELECT * FROM example")

for i, row in enumerate(cur.fetchall()):

	print("Usuario {}".format(i))
	print("\tNombre: {}".format(row[0]))
	print("\tEdad: {}".format(row[1]))

db.close()
