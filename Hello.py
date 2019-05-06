from flask import Flask, redirect, url_for, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='template')

l1 = list()
for i in range(8):
    l1.append({"id": i, "description": f"Desc {i}", "done": (i+i*i)/2 % 2 == 0})


def passwordchk(psw):
    if psw == 'Hello':
        flash("Logged In Successsfully")
        return 'todo'
    else:
        flash("Wrong Usrname/Password")
        return 'wrongpsw'


# SQL ALCHAEMY DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo_operations.sqlite3'
# Initialize DB
db = SQLAlchemy(app)


class todo_list(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    done = db.Column(db.Boolean)


def __init__(self, description, done):
    self.description = description
    self.done = done


db.create_all()


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/gotologin')
def gotologin():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['uname']
        password = request.form['pwd']
        return redirect(url_for(passwordchk(password)))

    else:
        user = request.args.get('uname')
        password = request.args.get('pwd')
        return redirect(url_for(password))


@app.route('/wrongpsw')
def wrongpsw():
    return render_template('login.html')


@app.route('/todo')
def todo():
    return render_template('todo.html')


@app.route('/printdict', methods=['GET', 'POST'])
def printdict():
    choice = request.form['action']
    a = int(choice[-1])
    result = l1[a-1]

    return render_template("finaloutput.html", result=result)


if __name__ == '__main__':
    app.run(port=5051, debug=True)
