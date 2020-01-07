from flask import Flask, render_template,request,redirect,url_for
import os
import main
import update_file
import insert_rec
import search_db

PEOPLE_FOLDER = os.path.join('static', 'photos')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
image_details=[]
#@app.route('/')
@app.route('/',methods=['GET','POST'])
def register():
	msg=[]
	if request.method == 'GET':

		print("registration form")
		return render_template("register.html")
	if request.method == 'POST':
		print("Checking Authentication")
		user=request.form['uname']
		p=request.form['psw']
		#print(user)
		#print(p)
		msg=search_db.check_authentication(user,p)
		if len(msg)==0:
			comm="Incorrect username or password"
			return render_template("register.html",result=comm)
		else:
			return redirect(url_for('show_index'))
@app.route('/add_rec',methods=['GET','POST'])
def add_rec():
	if request.method == 'GET':
		print("Adding record")
		return render_template("student.html")
	if request.method == 'POST':
		print("Updating Database")
		name=request.form['nm']
		password=request.form['pass']
		print(name)
		print(password)
		msg=insert_rec.record_insert(name,password)
		#print(msg)
		return redirect(url_for('register'))
		
		
@app.route('/index',methods=['GET','POST'])
def show_index():
	if request.method == 'GET':
		print("hello")
		image_details= main.generate_image_path()
		print(image_details)
		full_filename = os.path.join(app.config['UPLOAD_FOLDER'],image_details[2])
		return render_template("index.html",user_image=full_filename,eng_caption=image_details[3],mal_caption=image_details[4],image_id=image_details[1],caption_id=image_details[0])
	if request.method=='POST':
		post_arr=[]
		post_arr.append(request.form['corre_caption'])
		post_arr.append(request.form['image_id'])
		#print(image_details)
		msg=update_file.file_update(post_arr)
		print(msg)
		return redirect(url_for('show_index'))
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=5000)
