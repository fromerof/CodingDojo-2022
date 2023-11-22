from flask_app import app
import re 
from flask import render_template,request,redirect,flash,session
from flask_app.models.user import User
#from flask_app.models.message import Message
from flask_bcrypt import Bcrypt      
bcrypt = Bcrypt(app)
app.secret_key = "sssshhh"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data) 
    session['user_id'] = user_id
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    data = {
        "email": request.form['email'],
        "password": request.form['password']
    }
    user_in_db = User.get_by_email(data)
    
    if not bcrypt.check_password_hash(user_in_db[0]['password'], request.form['password']):
        print("usuario contiene data")
        flash("Invalid Email/Password",'invalid')
        return redirect('/')
    if not user_in_db:
        flash("Invalid Email/password")
        return redirect('/')
    session['user_id'] = user_in_db[0]['id']
    return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("dashboard.html")
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')