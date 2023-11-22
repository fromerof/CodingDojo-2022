from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Email:
    def __init__(self, data)
        self.data = data['id']
        self.email = data['email']
        self.created_at = data['creataed_at']
        self.updated_at = data['updated_at']

    @classmethod
    def email(cls):
        query = "INSERT INTO email"