from flask import Flask, request, jsonify
from flask_restx import Resource, Namespace
from database.database import Database
import pymysql

user = Namespace('user')


@user.route('', methods=['GET'])
class UserManagement(Resource):
    def get(self):
        database = Database()

        ID = request.args.get('id')
        PW = request.args.get('password')

        isID_v = ()
        isPW_v = ()

        sql = "SELECT * FROM server_study.user WHERE id = %s;"
        isID = database.execute_all(sql, ID)
        if isID != ():
             isID_v = list(isID[0].values())

        sql = "SELECT * FROM server_study.user WHERE pw = %s;"
        isPW = database.execute_all(sql, PW)
        if isPW != ():
             isPW_v = list(isPW[0].values())

        print(isID, isID_v, type(isID), type(isID_v))
        print(ID, PW)

        if isID == () and isPW == ():
            database.close()
            return {
                'message':"해당 유저가 존재하지 않음"
            },400
        elif (isID != () and isID_v[1] != PW) or (isPW != () and isPW_v[0] != ID):
            database.close()
            return {
                'message':'아이디나 비밀번호 불일치'
            }, 400
        
        sql = "SELECT nickname FROM server_study.user WHERE id = %s"
        nick = database.execute_one(sql, ID)
        database.close()
        return nick,200
    
@user.route('', methods=['POST'])
class UserManagement(Resource):
    def post(self):
         database = Database()

         dic = request.get_json()
         v_lst = list(dic.values())

         row_v = ()
         
         sql = "SELECT pw FROM server_study.user;"
         row = database.execute_all(sql)
         if row != ():
             row_v = list(row[0].values())

         print(row_v)

         for i in row_v:
             if i == v_lst[1]:
                 database.close()
                 return {
                     'is_success':False, 
                     'message':"이미 있는 유저"
                     }, 400

         
         sql = "INSERT INTO server_study.user VALUES(%s, %s, %s);"
         database.execute(sql, (v_lst[0], v_lst[1], v_lst[2]))
         database.commit()

         print(row)

         database.close()
         return {
             'is_success':True,
             'message':"유저 생성 성공"
             }, 200       
     
@user.route('', methods=['PUT'])
class UserManagement(Resource):
    def put(self):
         database = Database()

         dic = request.get_json()
         v_lst = list(dic.values())

         isID_v = ()
         isPW_v= ()
        
         sql = "SELECT * FROM server_study.user WHERE id = %s;"
         isID = database.execute_all(sql, v_lst[0])
         if isID != ():
             isID_v = list(isID[0].values())

         sql = "SELECT * FROM server_study.user WHERE pw = %s;"
         isPW = database.execute_all(sql, v_lst[1])
         if isPW != ():
             isPW_v = list(isPW[0].values())

         if (isID != () and isID_v[1] != v_lst[1]) or (isPW != () and isPW_v[0] != v_lst[0]) or (isID == () and isPW == ()):
             database.close()
             return {
                 'is_success':False,
                 'message':"아이디나 비밀번호 불일치"
             }, 400
         
         if isID != ():
              if (isID_v[2] == v_lst[2]):
                   database.close()
                   return {
                         'is_success':False,
                         'message':"현재 닉네임과 같음"
                     }, 400
         
         sql = "UPDATE server_study.user SET nickname = %s WHERE id = %s;"
         database.execute(sql, (v_lst[2], v_lst[0]))
         database.commit()

         database.close()
         return {
             'is_success':True,
             'message':"유저 닉네임 변경 성공"
         }, 200
    
@user.route('', methods=['DELETE']) 
class UserManagement(Resource):   
    def delete(self):
         database = Database()

         dic = request.get_json()
         v_lst = list(dic.values())

         sql = "SELECT * FROM server_study.user WHERE id = %s;"
         isID = database.execute_all(sql, v_lst[0])
         if isID != ():
             isID_v = list(isID[0].values())

         sql = "SELECT * FROM server_study.user WHERE pw = %s;"
         isPW = database.execute_all(sql, v_lst[1])
         if isPW != ():
             isPW_v = list(isPW[0].values())
                      

         if (isID != () and isID_v[1] != v_lst[1]) or (isPW != () and isPW_v[0] != v_lst[0]) or (isID == () and isPW == ()):
             database.close()
             return {
                 'is_success':False,
                 'message':"아이디나 비밀번호 불일치"
             }, 400
             

         sql = "DELETE FROM server_study.user WHERE id = %s AND pw = %s;"
         database.execute(sql, (v_lst[0], v_lst[1]))
         database.commit()

         database.close()
         return {
             'is_success':True,
             'message':"유저 삭제 성공"
         }, 200