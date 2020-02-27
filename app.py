from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from dataclasses import dataclass
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
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
        product_list = list(map(self._from_document_to_product, products))
        return jsonify(product_list)

    def _from_document_to_product(self, product):
        return Product(id=str(product.get('_id')), title=product.get('title'), 
        description=product.get('description'), price=product.get('price'))

class CreateProduct(Resource):
    def post(self):
        data = request.get_json()
        inserted = productsCollection.insert_one(data)
        return str(inserted.inserted_id)

class DeleteProduct(Resource):
    def delete(self, id):
        productsCollection.delete_one({ "_id": ObjectId(id) })

class AdminCheck(Resource):
    def post(self):
        adminPass = 'pass'
        data = request.get_json()
        if data['adminPass'] == adminPass:
            response = {'admin': True}
        else:
            response = {'admin': False}
        
        return jsonify(response)


#data classes
@dataclass(frozen=True)
class Product:
    id: str
    title: str
    description: str
    price: float


api.add_resource(Red, '/color/red')
api.add_resource(Blue, '/color/blue')
api.add_resource(Green, '/color/green')
api.add_resource(Yellow, '/color/yellow')
api.add_resource(White, '/color/')
api.add_resource(GetAllProducts, '/products')
api.add_resource(CreateProduct, '/products')
api.add_resource(DeleteProduct, '/products/<id>')
api.add_resource(AdminCheck, '/admin/check')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)