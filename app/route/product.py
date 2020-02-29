from flask import jsonify, request
from flask_restful import Resource

from app.dao.dao import ProductDao

productDao = ProductDao()

class GetAllProducts(Resource):
    def get(self):
        product_list = productDao.getAll()

        return jsonify(product_list)

class CreateProduct(Resource):
    def post(self):
        data = request.get_json()
        return productDao.create(data)

class DeleteProduct(Resource):
    def delete(self, id):
        productDao.delete(id)