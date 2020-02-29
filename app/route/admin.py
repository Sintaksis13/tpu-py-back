from flask import jsonify, request
from flask_restful import Resource

class AdminCheck(Resource):
    def post(self):
        adminPass = 'pass'
        data = request.get_json()
        if data['adminPass'] == adminPass:
            response = {'admin': True}
        else:
            response = {'admin': False}
        
        return jsonify(response)