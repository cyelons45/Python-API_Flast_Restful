import sqlite3
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def findbyusername(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def findbyid(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='Username is required'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='Password is required'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.findbyusername(data['username']):
            return {"message": "A user with this username already exist"}, 400
        connection = sqlite3.connect('data.db')
        print("Opened database successfully")
        cursor = connection.cursor()
        query = "INSERT INTO users VALUES (NULL,?,?)"
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {"message": "Usere created successfully"}


# if __name__ == '__main__':
#     # res = User.findbyusername('jose')
#     res = User.findbyid(3)
#     print(res.__dict__)
