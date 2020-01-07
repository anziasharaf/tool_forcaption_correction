#!/usr/bin/python
import mysql.connector


#image_details=main.generate_image_path()
#print(image_details)
def file_update(image_details):
	#print(image_details)
	mydb = mysql.connector.connect(
  		host="localhost",
		database="image_tool",
  		port=3306,
  		user="root",
 		passwd="123456")
	#print(image_details[1])
	corr_caption=image_details[0]
	print("corrected caption######")
	print(corr_caption)
	caption_id=image_details[1]
	#sql_select_query = "select * from image_details where caption_id = caption_id"
	#cursor = mydb.cursor()
	#cursor.execute(sql_select_query)
	#record = cursor.fetchone()
	#print (record)
	
	if corr_caption=='':
		print("corr_caption")
		f=0
	else:
		f=2
	
	print("flag")
	print(f)
	#f=str(f)

	sql_update_query="Update image_details set corrected_caption= %s ,flag = %s where caption_id = %s "
	val=(corr_caption ,f,caption_id)
	cursor=mydb.cursor()
	cursor.execute(sql_update_query,val)
	mydb.commit()
	print ("Record Updated successfully ")
	#print(corr_caption)
	#print(caption_id)
	message="Malayalam caption is updated"
	return message
