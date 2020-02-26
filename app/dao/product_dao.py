from pymongo import MongoClient

class ProductEntityDao():
	def __init__(self):
		self.client = MongoClient("localhost", 27017)
		self.database = client['tputask']

	def create(self, productEntity):
		return db.products.insert_one(productEntity).inserted_id

	def get(self):
		return db.products.find()
