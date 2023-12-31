from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template,request,redirect,flash,session
from flask_app.models.user import User
from flask_app.models.message import Message


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
    user_in_db = User.get_by_email(request.form)
    if not user_in_db:
        flash("Invalid Email/password")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    print("HOLA MUNDO")
    user = User.user_login(data)
    messages = Message.get_user_messages(data)
    print("por buen camino")
    users = User.get_all()
    print("PASO GET ALL")
    return render_template("dashboard.html",user = user,messages = messages, users = users)
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')