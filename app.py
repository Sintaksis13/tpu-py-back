from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Red:
    def get(self):
        return jsonify({'color': 'red'})

class Blue:
    def get(self):
        return jsonify({'color': 'blue'})

class Green:
    def get(self):
        return jsonify({'color': 'green'})

class Yellow:
    def get(self):
        return jsonify({'color': 'yellow'})

class White:
    def get(self):
        return jsonify({'color': 'white'})

app.add_resource(Red, '/color/red')
app.add_resource(Red, '/color/blue')
app.add_resource(Red, '/color/green')
app.add_resource(Red, '/color/yellow')
app.add_resource(Red, '/color')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)