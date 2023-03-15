from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL
import json
app=Flask(__name__)
app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="hello"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route('/index.html')
@app.route('/index')
@app.route('/')
def home():
    cur=mysql.connection.cursor()
    cur.execute("select * from userdata order by Name ")
    val=cur.fetchall()
    return render_template("index.html",datas=val)


@app.route('/edit/')
def edit():
    cur=mysql.connection.cursor()
    cur.execute("select * from userdata order by Name")
    val=cur.fetchall()
    return render_template("edit.html",datas=val)

@app.route('/save_edit/<string:name>',methods=["POST",'GET'])
def save_edit(name):
    cur = mysql.connection.cursor()

    if(request.method=="POST"):
        print('hello')
        Name=request.form['Name']
        Chemistry = request.form['Chemistry']
        Physics = request.form['Physics']
        Maths = request.form['Maths']
        cur.execute("update userdata set Name=%s, Chemistry=%s, Physics=%s, Maths=%s where Name=%s",(Name,Chemistry,Physics,Maths,name))
        mysql.connection.commit()
    cur.execute("select * from userdata order by Name")
    data = cur.fetchall()

    return redirect(url_for("edit"))

@app.route("/save_req/<string:name>")
def save_req(name):
    cur = mysql.connection.cursor()
    cur.execute("select * from userdata order by Name")
    data = cur.fetchall()
    return render_template("save_req.html", datas=data,name=name)

@app.route("/del_rec/<string:name>")
def del_rec(name):
    cur = mysql.connection.cursor()
    cur.execute("delete from userdata where Name=%s",(name,))
    cur.execute("select * from userdata order by Name")
    data = cur.fetchall()
    mysql.connection.commit()
    return redirect(url_for("edit"))

@app.route("/add_names/",methods=["POST","GET"])
def add_names():
    cur = mysql.connection.cursor()
    if (request.method == "POST"):
        print(request.form.get(''))
        Name = request.form['Name1']
        Chemistry = request.form['Chemistry']
        Physics = request.form['Physics']
        Maths = request.form['Maths']
        cur.execute("insert into userdata values (%s,%s,%s,%s)",
                    (Name, Chemistry, Physics, Maths))
        mysql.connection.commit()
        print(123465)
    cur.execute("select * from userdata order by Name")
    data = cur.fetchall()

    return redirect(url_for("edit"))

@app.route('/word/<string:w>')
def word(w):
    return render_template("temp.html",word=w)
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")

"""
from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="hello"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template("demo.html")

@app.route("/list.html")
@app.route("/list")
def list():
    cur=mysql.connection.cursor()
    cur.execute("select * from hello.userdata")
    val=cur.fetchall()
    return render_template("notlist.html",datas=val)

@app.route("/addUser")
def addUser():
    cur = mysql.connection.cursor()
    cur.execute("select * from hello.userdata")
    val = cur.fetchall()
    return render_template("addUser.html",datas=val)

@app.route("/confirm",methods=["POST",'GET'])
def confirm():
    if request.method=="POST":
        try:
            cur=mysql.connection.cursor()
            username=request.form["username"]
            Maths=request.form["Maths"]
            Chemistry=request.form["Chemistry"]
            Physcis=request.form["Physcis"]
            print('insert into userdata values(%s,%s,%s,%s)',(username,Maths,Chemistry,Physcis))
            cur.execute('insert into userdata values(%s,%s,%s,%s)',(username,Maths,Chemistry,Physcis))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for("home"))
        except:
            return redirect(url_for("list"))
@app.route('/images')
@app.route('/images.html')
def image():
    cur=mysql.connection.cursor()
    cur.execute("select * from images")
    val=cur.fetchall()
    return render_template("images.html",datas=val)


@app.route('/delete/<string:id>',methods=['POST','GET'])
def delete(id):
    if request.method=='GET':
        cur = mysql.connection.cursor()
        print(id)
        cur.execute("delete from userdata where username=%s",(id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('home'))
    return redirect(url_for('list'))
if __name__=="__main__":
    app.run(debug=True)"""