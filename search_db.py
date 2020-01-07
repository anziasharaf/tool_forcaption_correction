import mysql.connector
def check_authentication(user_name,pass_word):
	mydb = mysql.connector.connect(
			host="localhost",
			database="image_tool",
			port=3306,
			user="root",
			passwd="123456")
	mycursor = mydb.cursor()
	#user_name=input("enter user name")
	#pass_word=input("enter your password") 

	sql_query =  "select username,password from register where username=  %s and password =%s "
	val=(user_name,pass_word)
	cursor = mydb.cursor()
	cursor = mydb.cursor(buffered=True)
	cursor.execute(sql_query,val)
	records = cursor.fetchall()
	
	print(records)
	return (records)
