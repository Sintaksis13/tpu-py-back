from flask import jsonify
from flask_restful import Resource

from app.dao.dao import LogDao

class Log(Resource):
    logDao = LogDao()

    def get(self):
        logs = self.logDao.getAll()
        return jsonify(logs)