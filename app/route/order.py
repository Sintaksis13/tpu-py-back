from flask import jsonify, request
from flask_restful import Resource

from app.dao.dao import OrderDao

orderDao = OrderDao()

class CreateOrder(Resource):
    def post(self):
        data = request.get_json()
        return orderDao.create(data)

class GetAllOrders(Resource):
    def get(self):
        order_list = orderDao.getAll()
        return jsonify(order_list)

class GetOrder(Resource):
    def get(self, id):
        order = orderDao.getById(id)
        return jsonify(order)