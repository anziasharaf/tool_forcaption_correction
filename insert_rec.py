import mysql.connector
def record_insert(name,password):
	mydb = mysql.connector.connect(
			host="localhost",
			database="image_tool",
			port=3306,
			user="root",
			passwd="123456")
	mycursor = mydb.cursor()
	sql_query = "INSERT INTO register (username, password) VALUES (%s, %s)"
	val = (name, password)
	mycursor.execute(sql_query, val)
	mydb.commit()
	print(mycursor.rowcount, "record inserted.")
	msg="New record inserted"
	return(msg)
