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


BOOKS = {
    "BOOK_1": "Hadoop The Definitive Guide By Tom White 1st edition Orielly Jun 2009",
    "BOOK_2": "Hadoop in Practice by Alex Holmes Manning 2012",
    "BOOK_3": "Learning Hadoop 2 - Garry Turkington PACKET Feb 2015",
    "BOOK_4": "Hadoop Real-World Solutions Cookbook By Jonathan R. Owens PACKT Feb 2013",
    "BOOK_5": "Hadoop Application Architectures By Mark Grover Jul 2015 Orielly"
}

request_responses = {200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error',
                     503: 'Internal Server Error', 404: 'Not Found'}


@api_name_space.route("/book/<string:book_id>")
class BookApi(Resource):
    @app_api.doc(responses=request_responses,
                 params={'book_id': 'Specify the Id associated with the book'}
                 )
    def get(self, **kwargs):
        try:
            book_id = kwargs.get('book_id', "")
            if book_id in BOOKS:
                return {"book": BOOKS[book_id], "book_id": book_id}, 200
            else:
                return "Book not found", 404
        except Exception as ex:
            return ex.__str__(), 503


if __name__ == '__main__':
    flask_app.run(debug=True)
