import MySQLdb as m

db = m.connect(host="localhost", user="root", passwd="mysql98")
cur = db.cursor()

cur.execute("Create database election")
cur.execute("commit;")