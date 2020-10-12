from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api= Api(app)
app.configP['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db=SQLAlchemy(app)


class DataModel(db.Model):
    id = db.Column(db.integer,primary_key=True)
    name=db.Column(db.String(100),nullible=False)
    views=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"Data(name={name},test={test}"

db.create_all()

data_put_args = reqparse.RequestParser()
data_put_args.add_argument("name",type=str)
data_put_args.add_argument("test",type=int)

class Data(Resource):
    def get(self,name,test):
        return{"name":name,"test":test}

    def post(self,data_id):
        args=data_put_args.parse_args()
        return {data_id:args}

api.add_resource(Hell,"/hell/<string:name>/<int:test>")

if __name__=="__main__":
    app.run(debug=True)