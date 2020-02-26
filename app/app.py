from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from first_lab.routes import routes

app = Flask(__name__)
api = Api(app)

for route, path in routes:
    print(route + ', ' + path + '\n')
    app.add_resource(route, path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)