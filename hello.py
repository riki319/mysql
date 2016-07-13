import MySQLdb

from config import data

db = MySQLdb.connect(**data)

cur = db.cursor()


cur.execute("SELECT * FROM potluck")

for row in cur.fetchall():

	print row[0]

db.close()
