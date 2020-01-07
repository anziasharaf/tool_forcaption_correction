#!/usr/bin/python
import mysql.connector
import random
def generate_image_path():
	#f1=open("/home/user/Desktop/tool_for_caption_correction/out.csv","r")
	mydb = mysql.connector.connect(
		host="localhost",
		database="image_tool",
		port=3306,
		user="root",
		passwd="123456"
	)
	sql_select_Query = "select * from image_details where flag=0 "
	cursor = mydb.cursor()
	cursor = mydb.cursor(buffered=True)
	cursor.execute(sql_select_Query)
	records = cursor.fetchmany(50)
	#print(records)
	a=random.randint(0,50)
	m=records[a]
	print(m)
	image_id=m[1]
	caption_id=m[0]
	eng_caption=m[2]
	mal_caption=m[3]
	
	#print("caption_id")
	
	
	f=1
	my_image=mydb.cursor()
	sql_update_query="Update image_details set flag = %s where caption_id = %s "
	val=(f,caption_id)
	my_image.execute(sql_update_query,val)
	mydb.commit()
	
	
	#print("Total number of rows in python_developers is - ", cursor.rowcount)
	#print(records)
	#l=records[0]
	#l=f1.readlines()
	details=[]
	#a=random.randint(0,50)
	#print(a)
	str1="COCO_train2014_"
	str3=".jpg"
	#m=records[0]
	#image_id=records[0]
	#caption_id=records[1]
	#eng_caption=records[2]
	#mal_caption=records[3]
	s=str(image_id)
	str2=s.rjust(12,'0')
	st=str1+str2+str3
	#print(st)
	#details.append(a)
	details.append(image_id)
	details.append(caption_id)
	details.append(st)
	details.append(eng_caption)
	details.append(mal_caption)
	#print(details)
	#cursor.close()
	return(details)
