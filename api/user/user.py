from flask import Flask, request
from flask_restx import Resource, Namespace
from database.database import Database

user = Namespace('user')

@user.route('')
class UserManagement(Resource):
    def get(self):
        # GET method 구현 부분
        return { "nickname": "test" }

    def post(self):
        # POST method 구현 부분
        return {}

    def put(self):
        # PUT method 구현 부분
        return {}
    
    def delete(self):
        # DELETE method 구현 부분
        return {}