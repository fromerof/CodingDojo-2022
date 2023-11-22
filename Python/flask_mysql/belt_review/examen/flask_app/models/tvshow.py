from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


class Tvshow:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def get_user_messages(cls,data):
        query = "SELECT users.first_name as sender, users2.first_name as reciever, messages.* FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.reciever_id WHERE users2.id = %(id)s;"
        results = connectToMySQL("belt_exam").query_db(query,data)
        messages = []
        for message in results:
            messages.append(cls(message))
        return messages
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO tvshows (title,network,release_date,description,created_at,updated_at,user_id) VALUES (%(title)s,%(network)s,%(release_date)s,%(description)s,NOW(),NOW(),%(user_id)s);"
        results = connectToMySQL("belt_exam").query_db(query,data)
        return results

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM tvshows WHERE id = %(tvshow_id)s;"
        results = connectToMySQL("belt_exam").query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tvshows"
        results = connectToMySQL("belt_exam").query_db(query)
        tvshows = []
        for tv in results:
            tvshows.append(cls(tv))
        return tvshows

    @classmethod
    def update(cls, data):
        query = "UPDATE tvshows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s,description=%(description)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL("belt_exam").query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM tvshows WHERE id = %(id)s;"
        return connectToMySQL("belt_exam").query_db(query,data)
    
    @staticmethod
    def validate_tvshow(tvshow):
        is_valid = True
        if len(tvshow['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters ","tvshow")
        if len(tvshow['network']) < 3:
            is_valid = False
            flash("Network must be at least 3 characters","tvshow")
        if len(tvshow['release_date']) == "":
            is_valid = False
            flash("release date must have a date","tvshow")
        if len(tvshow['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","tvshow")
        return is_valid
