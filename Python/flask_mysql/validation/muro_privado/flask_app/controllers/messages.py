from flask_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
from flask import render_template,request,redirect,flash,session
from flask_app.models.user import User
from flask_app.models.message import Message


@app.route('/post_message',methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "content": request.form['content'],
        "sender_id":  request.form['sender_id'],
        "reciever_id": request.form['reciever_id']
        
    }
    print("PASO POR ACA?")
    Message.save(data)
    print("PASO POR ACA?")
    return redirect('/dashboard')

@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy(data)
    return redirect('/dashboard')