from flask import Flask, request
from flask_restx import Resource, Namespace
from database.database import Database
import pymysql

user = Namespace('user')


@user.route('/user')
class UserManagement(Resource):
    def get(self):
        dic = request.get_json()
        v_lst = list(dic.values())

        return {}

    def post(self):
        dic = request.get_json()
        v_lst = list(dic.values())

        sql = "INSERT INTO study (id, pw, nickname) VALUES(%s, %s, %s)"
        Database.execute(sql, (v_lst[0], v_lst[1], v_lst[2]))

        if request.status_code == 200:
            isSuccess = True
            message = "유저 생성 성공"
        elif request.status_code == 400:
            isSuccess = False
            message = "이미 있는 유저"

        return {  
            'is_success':isSuccess,
            'message':message
        }

    def put(self):
        # PUT method 구현 부분
        return {

        }
    
    def delete(self):
        
        return {}