from flask import Flask  #1
from flask_restful import Api   #3
from employee import Employee,SpecificEmp   #5



app = Flask(__name__)   #2
api = Api(app)      #4

api.add_resource(Employee,"/employee")
api.add_resource(SpecificEmp,'/emp/<string:emp_id>')

if __name__ == '__main__':
    app.run(port=8080,debug=True)


