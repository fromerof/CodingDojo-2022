
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash,request


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# PSW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
PSW_REGEX =  re.compile(r'^[A-Za-z0-9@#$%^&+=]{8,}$')
class User:
    def __init__(self, data):
        self.first_name = data['first_name'],
        self.last_name = data['last_name'],
        self.email = data['email'],
        self.password = data['password'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL("muro_privado").query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("muro_privado").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])


    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("muro_privado").query_db(query,user)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(user["first_name"]) < 3:
            flash("First_name must be at least 3 characters")
            is_valid = False
        if len(user["last_name"]) < 3:
            flash("Last_name must be at least 3 characters")
            is_valid = False
        if not PSW_REGEX.match(user['password']):
            flash("Invalid password!")
            is_valid = False
        if user["password"] != user["confirm"]:
            flash("Password don't match")
        return is_valid