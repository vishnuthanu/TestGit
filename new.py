import pymysql
from flask import Flask, render_template, request,flash
from pymysql import cursors
app = Flask(__name__,template_folder='template')

db = pymysql.connect(host='localhost',user='root',password='',db='work',charset='utf8',use_unicode=True)
cursor1 = db.cursor(cursors.DictCursor)
cursor = db.cursor()

@app.route('/input',methods=['GET','POST'])
def get_data():
	if request.method == 'POST':
		ID=request.form['id']
		Name=request.form['name']
		Lname=request.form['lname']
		Age=request.form['age']
		sql = """INSERT INTO demo(id,name,lname,age) VALUES(%s,%s,%s,%s)"""
		cursor.execute(sql,(ID,Name,Lname,Age))
		db.commit()
		print("Successfully insert")
	return render_template("form1.html")

@app.route('/view')
def view_data():
	cursor1.execute("select*from demo")
	results = cursor1.fetchall()
	print(results)
	return render_template("view.html", results=results)

@app.route('/delete')
def delete_user():
	id=request.args.get('id')
	cursor.execute("DELETE FROM demo WHERE id=%s", (id))
	db.commit()
	print("Successfuly delete")
	return render_template("form1.html")
	cursor.close()
	db.close()
@app.route('/edit')
def edit():
	id=request.args.get('id')
	sel="select * from demo where id=%s"
	cursor1.execute(sel,(id))
	result = cursor1.fetchall()
	print (result)
	return render_template('form2.html', res=result)


@app.route('/update',methods=['post'])
def update():
	ID=request.form['id']
	Name=request.form['name']
	Lname=request.form['lname']
	Age=request.form['age']
	upd="UPDATE demo SET name = %s, lname = %s, age = %s WHERE id = %s"
	cursor.execute(upd,(Name, Lname,Age,ID))
	result = cursor.fetchall()
	print(result)
	db.commit()
	return render_template('form1.html',res=result)
	return 'updated'
	cursor.close() 
	db.close()
			


if __name__ == "__main__":
	app.run(debug=True)



