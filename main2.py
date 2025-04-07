import mysql.connector

connection = mysql.connector.connect(user = 'root', database='evansPC', password = '2009evanjr')

connection.close()