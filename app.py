from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Red(Resource):
    def get(self):
        return jsonify({'color': 'red'})

class Blue(Resource):
    def get(self):
        return jsonify({'color': 'blue'})

class Green(Resource):
    def get(self):
        return jsonify({'color': 'green'})

class Yellow(Resource):
    def get(self):
        return jsonify({'color': 'yellow'})

class White(Resource):
    def get(self):
        return jsonify({'color': 'white'})

api.add_resource(Red, '/color/red')
api.add_resource(Red, '/color/blue')
api.add_resource(Red, '/color/green')
api.add_resource(Red, '/color/yellow')
api.add_resource(Red, '/color')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)