import sqlite3
from flask_restful import Resource
from flask import request

class Employee(Resource):

    def post(self):
        data = request.get_json()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM EMPLOYEE WHERE emp_name=? AND doj=?"
        result =cursor.execute(query,(data['emp_name'],data['doj']))
        row = result.fetchone()
        if row:
            return {"msg":"employee already present in database!"},400
        else:
            query1 = "Insert into EMPLOYEE values(NULL,?,?,?)"
            cursor.execute(query1,(data['emp_name'],data['project_name'],data['doj']))
            connection.commit()
            connection.close()
            return {"msg": "successfully added"},200

    def put(self):
        data = request.get_json()
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query1 = "select * from EMPLOYEE where emp_id=?"
        result=cursor.execute(query1,(data['emp_id'],))
        row = result.fetchone()
        if row:
            query = "update EMPLOYEE set project_name=? where emp_id=?"
            cursor.execute(query,(data['project_name'],data['emp_id']))
            connection.commit()
            connection.close()
            return {"msg": "updated"}
        else:
            return {"msg":"incorrect input"}


    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM EMPLOYEE"
        result = cursor.execute(query)
        row = result.fetchall()
        connection.commit()
        connection.close()
        return {"employees": row}




class SpecificEmp(Resource):
    def delete(self,emp_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query1 = "select * from EMPLOYEE where emp_id=?"
        result=cursor.execute(query1,(emp_id,))
        row=result.fetchone()
        if row:
            query = "delete from EMPLOYEE where emp_id=?"
            cursor.execute(query,(emp_id,))
            connection.commit()
            connection.commit()
            connection.close()
            return {"msg":"deleted!"}
        else:
            return {"msg":"incorrect employee id"}
