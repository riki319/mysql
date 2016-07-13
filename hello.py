import MySQLdb


db = MySQLdb.connect(host="localhost",
		    user="pwaqo",
		    passwd="pass",
		    db='example')

cur = db.cursor()


cur.execute("SELECT * FROM potluck")

for row in cur.fetchall():

	print row[0]

db.close()
