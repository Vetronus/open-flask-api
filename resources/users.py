import models
from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse, inputs
from playhouse.shortcuts import model_to_dict


class Users(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('email', required=True, help='No email provided', location=['form', 'json'])
        self.reqparse.add_argument('name', required=True, help='No name provided', location=['form', 'json'])
        self.reqparse.add_argument('password', required=True, help='No password provided', location=['form', 'json'])
        self.reqparse.add_argument('tag', required=False, location=['form', 'json'], default='AROXBIT is awesome !')
        super().__init__()

    def get(self):
        _users = []
        for temp_user in models.User.select():
            _user = model_to_dict(temp_user)
            _users.append(_user)

        return jsonify({'Users': _users})


    def post(self):
        args = self.reqparse.parse_args()
        models.User.create(**args)
        return jsonify(args)



class User(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('tag', required=False, location=['form', 'json'], default='AROXBIT is awesome !')
        super().__init__()

    def get(self, id):
        temp_user = models.User.select().where(models.User.email==id).first()
        _user = model_to_dict(temp_user)
        return jsonify(_user)

    def put(self, id):
        args = self.reqparse.parse_args()
        # models.User.create(**args)
        _q = models.User.update(**args).where(models.User.email == id)
        _q.execute()
        return jsonify({'response': 'updated'})

    def delete(self, id):
        _q = models.User.delete().where(models.User.email==id)
        _q.execute()
        return jsonify({'response': 'deleted'})





users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(Users, '/users', endpoint='users')
api.add_resource(User, '/users/<id>', endpoint='user')