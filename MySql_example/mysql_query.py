import mysql.connector

cnx = mysql.connector.connect(
    user='steven', 
    password='Steelcar889@', 
    host='192.168.1.110', 
    database='gitea')

cursor = cnx.cursor()

query = ("SELECT user, host FROM mysql.user")

cursor.execute(query)

for user, host in cursor:
    print("{} {}".format(user, host))
