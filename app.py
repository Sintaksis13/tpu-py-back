from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin

from app.route.first_lab import *
from app.route.admin import AdminCheck
from app.route.product import *
from app.route.order import *
from app.route.log import Log

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
api = Api(app)


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

api.add_resource(Log, '/logs')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)