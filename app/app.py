from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from first_lab.routes import routes

app = Flask(__name__)
api = Api(app)

for route, path in routes:
    app.add_resource(route, path)

if __name__ == "__main__":
    app.run(host='localhost:8080', debug=True)