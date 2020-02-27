from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
api = Api(app)
client = MongoClient('mongodb://db:27017')
db = client.projectDB

#collections
productsCollection = db['product']


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

class GetAllProducts(Resource):
    def get(self):
        products = productsCollection.find()
        product_list = list(products)
        print(product_list)
        return jsonify({'products': product_list})

class AdminCheck(Resource):
    def get(self):
        adminPass = 'pass'
        data = request.get_json()
        if data['adminPass'] == adminPass:
            response = {'admin': True}
        else:
            response = {'admin': False}
        
        return jsonify(response)

api.add_resource(Red, '/color/red')
api.add_resource(Blue, '/color/blue')
api.add_resource(Green, '/color/green')
api.add_resource(Yellow, '/color/yellow')
api.add_resource(White, '/color/')
api.add_resource(GetAllProducts, '/products')
api.add_resource(AdminCheck, '/admin/check')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)