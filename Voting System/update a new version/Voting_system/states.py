import MySQLdb as m

db = m.connect(host = "localhost", user="root", passwd="wsu12345", db="election")
cur = db.cursor()

cur.execute("Create table countvotes (name varchar(50), count int)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Java',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('Python',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('C++',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('HTML',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('R',0)")
cur.execute("commit;")
cur.execute("Insert into countvotes(name,count) Values('JavaScript',0)")
cur.execute("commit;")