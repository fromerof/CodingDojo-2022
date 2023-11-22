from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.tvshow import Tvshow
from flask_app.models.user import User


@app.route('/add/tvshow/')
def add_tvshow():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('create_tvshow.html',user=User.get_by_id(data))

@app.route('/create/tvshow/',methods=['POST'])
def create_tvshow():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tvshow.validate_tvshow(request.form):
        return redirect('/add/tvshow/')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "user_id": session["user_id"]
    }
    Tvshow.save(data)
    return redirect('/dashboard')

@app.route('/tvshow/<int:id>')
def show_tvshow(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "tvshow_id":id
    }
    user_data = {
        "id":session['user_id']
    }
    print("id")
    return render_template("show_tvshow.html",tvshow=Tvshow.get_one(data),user=User.get_by_id(user_data))


@app.route('/edit/tvshow/<int:tvshow_id>')
def edit_recipe(tvshow_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "tvshow_id":tvshow_id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_tvshow.html",edit=Tvshow.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/tvshow/',methods=['POST'])
def update_tvshow():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tvshow.validate_tvshow(request.form):
        return redirect('/edit/tvshow/')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "id": request.form['id']
    }
    Tvshow.update(data)
    return redirect('/dashboard')

@app.route('/delete/tvshow/<int:id>')
def delete_tvshow(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Tvshow.delete(data)
    return redirect('/dashboard')