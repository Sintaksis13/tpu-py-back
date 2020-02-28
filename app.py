from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
from dataclasses import dataclass
from bson.objectid import ObjectId
from typing import List

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
api = Api(app)
client = MongoClient('mongodb://localhost:27017')
db = client.projectDB

#collections
productsCollection = db['product']
ordersCollection = db['order']


#First lab
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

#Second lab
#Product
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

#Order
class CreateOrder(Resource):
    def post(self):
        data = request.get_json()
        inserted = ordersCollection.insert_one(data)
        id = str(inserted.inserted_id)
        print(id)
        return id

class GetAllOrders(Resource):
    def get(self):
        orders = ordersCollection.find()
        order_list = list(map(self._from_document_to_order, orders))
        return jsonify(order_list)

    def _from_document_to_order(self, order):
        return Order(id=str(order.get('_id')), orderLines=order.get('orderLines'), 
            totalAmount=order.get('totalAmount'), customerData=order.get('customerData'))

class GetOrder(Resource):
    def get(self, id):
        if "\"" in id:
            id = id[1:-1] 
        order = ordersCollection.find_one({ "_id": ObjectId(id) })
        print(order)
        orderLines = order.get('orderLines')
        print(orderLines)
        richOrderLines = list(map(self._enrichOrderLines, orderLines))
        print(richOrderLines)
        richOrder = RichOrder(id=str(order.get('_id')), orderLines=richOrderLines, 
            totalAmount=order.get('totalAmount'), customerData=order.get('customerData'))
        return jsonify(richOrder)

    def _enrichOrderLines(self, orderLine):
        product = productsCollection.find_one({ "_id": ObjectId(orderLine.get('productId')) })
        entity = self._from_document_to_product(product)
        return RichOrderLine(product=entity, count=orderLine.get('count'))

    def _from_document_to_product(self, product):
        return Product(id=str(product.get('_id')), title=product.get('title'), 
            description=product.get('description'), price=product.get('price'))


#AdminCheck
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

@dataclass(frozen=True)
class OrderLine:
    productId: str
    count: int

@dataclass(frozen=True)
class CustomerData:
    name: str
    address: str
    phone: str

@dataclass(frozen=True)
class Order:
    id: str
    orderLines: List[OrderLine]
    totalAmount: float
    customerData: CustomerData

@dataclass(frozen=True)
class RichOrderLine:
    product: Product
    count: int

@dataclass(frozen=True)
class RichOrder:
    id: str
    orderLines: List[RichOrderLine]
    totalAmount: float
    customerData: CustomerData


#urls mapping
api.add_resource(Red, '/color/red')
api.add_resource(Blue, '/color/blue')
api.add_resource(Green, '/color/green')
api.add_resource(Yellow, '/color/yellow')
api.add_resource(White, '/color/')

api.add_resource(GetAllProducts, '/products')
api.add_resource(CreateProduct, '/products')
api.add_resource(DeleteProduct, '/products/<id>')

api.add_resource(CreateOrder, '/orders')
api.add_resource(GetAllOrders, '/orders')
api.add_resource(GetOrder, '/orders/<id>')

api.add_resource(AdminCheck, '/admin/check')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)