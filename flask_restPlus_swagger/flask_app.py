from flask import Flask, jsonify
from flask_restplus import Api, Resource

flask_app = Flask(__name__)
app_api = Api(app=flask_app)

api_name_space = app_api.namespace('api', description='This is a simple APIs')


@api_name_space.route("/")
class MainApis(Resource):
    def get(self):
        return jsonify({"message": "This is get method"})

    def post(self):
        return jsonify({"message": "this is post method"})


if __name__ == '__main__':
    flask_app.run()
