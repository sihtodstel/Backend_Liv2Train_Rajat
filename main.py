from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class dataModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"data(name = {name}, views = {views}, likes = {likes})"

data_put_args = reqparse.RequestParser()
data_put_args.add_argument("name", type=str, help="Name of the data is required", required=True)
data_put_args.add_argument("views", type=int, help="Views of the data", required=True)
data_put_args.add_argument("likes", type=int, help="Likes on the data", required=True)

data_update_args = reqparse.RequestParser()
data_update_args.add_argument("name", type=str, help="Name of the data is required")
data_update_args.add_argument("views", type=int, help="Views of the data")
data_update_args.add_argument("likes", type=int, help="Likes on the data")

resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}

class data(Resource):
	@marshal_with(resource_fields)
	def get(self, data_id):
		result = dataModel.query.filter_by(id=data_id).first()
		if not result:
			abort(404, message="Could not find data with that id")
		return result

	@marshal_with(resource_fields)
	def put(self, data_id):
		args = data_put_args.parse_args()
		result = dataModel.query.filter_by(id=data_id).first()
		if result:
			abort(409, message="data id taken...")

		data = dataModel(id=data_id, name=args['name'], views=args['views'], likes=args['likes'])
		db.session.add(data)
		db.session.commit()
		return data, 201

	@marshal_with(resource_fields)
	def patch(self, data_id):
		args = data_update_args.parse_args()
		result = dataModel.query.filter_by(id=data_id).first()
		if not result:
			abort(404, message="data doesn't exist, cannot update")

		if args['name']:
			result.name = args['name']
		if args['views']:
			result.views = args['views']
		if args['likes']:
			result.likes = args['likes']

		db.session.commit()

		return result


	def delete(self, data_id):
		abort_if_data_id_doesnt_exist(data_id)
		del datas[data_id]
		return '', 204


api.add_resource(data, "/data/<int:data_id>")

if __name__ == "__main__":
	app.run(debug=True)