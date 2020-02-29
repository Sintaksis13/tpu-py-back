from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

from app.domain.rich_order import RichOrder
from app.domain.rich_order_line import RichOrderLine
from app.domain.product import Product
from app.domain.order import Order
from app.domain.log import Log

client = MongoClient('mongodb://localhost:27017')
db = client.projectDB

class LogDao:
    collection = db['log']

    def create(self, message):
        log = {"date": datetime.datetime.now(), "message": message}
        inserted = self.collection.insert_one(log)

    def getAll(self):
        self.create("Был запрошен список журналов")
        logs = self.collection.find()
        return list(map(self._from_document_to_log, logs))

    def _from_document_to_log(self, document):
        return Log(id=str(document.get('_id')), 
        date=document.get('date'), message=document.get('message'))

class ProductDao:
    collection = db['product']
    logDao = LogDao()

    def getAll(self):
        self.logDao.create("Был запрошен список всех товаров")
        products = self.collection.find()
        product_list = list(map(self._from_document_to_product, products))
        return product_list

    def _from_document_to_product(self, product):
        return Product(id=str(product.get('_id')), title=product.get('title'), 
            description=product.get('description'), price=product.get('price'))

    def create(self, data):
        inserted = self.collection.insert_one(data)
        self.logDao.create("Администратором был создан новый товар (" + data.get('title') + ")")
        return str(inserted.inserted_id)

    def findById(self, id):
        self.logDao.create("Был запрошен товар с ID = " + id)
        product = self.collection.find_one({ "_id": ObjectId(id) })
        return product

    def delete(self, id):
        self.logDao.create("Администратором был удалён товар с ID = " + id)
        self.collection.delete_one({ "_id": ObjectId(id) })


class OrderDao:
    collection = db['order']
    productDao = ProductDao()
    logDao = LogDao()

    def create(self, data):
        inserted = self.collection.insert_one(data)
        if data.get('customerData') == None :
            self.logDao.create("Пользователь сделал заказ, но ещё не указал свои данные. ID = " 
            + str(inserted.inserted_id)) 
        else:
            self.logDao.create("Заказ пользователя был успешно создан ID = " 
            + str(inserted.inserted_id)) 
        return str(inserted.inserted_id)

    def getAll(self):
        self.logDao.create("Администратором был запрошен список всех заказов")
        orders = self.collection.find()
        order_list = list(map(self._from_document_to_order, orders))
        return order_list

    def getById(self, id):
        if "\"" in id:
            id = id[1:-1] 
        self.logDao.create("Был запрошен заказ с ID = " + id)
        order = self.collection.find_one({ "_id": ObjectId(id) })
        orderLines = order.get('orderLines')
        richOrderLines = list(map(self._enrichOrderLines, orderLines))
        richOrder = RichOrder(id=str(order.get('_id')), orderLines=richOrderLines, 
            totalAmount=order.get('totalAmount'), customerData=order.get('customerData'))
        return richOrder

    def _enrichOrderLines(self, orderLine):
        product = self.productDao.findById(orderLine.get('productId'))
        if product == None:
            return None
        entity = self._from_document_to_product(product)
        return RichOrderLine(product=entity, count=orderLine.get('count'))

    def _from_document_to_product(self, product):
        return Product(id=str(product.get('_id')), title=product.get('title'), 
            description=product.get('description'), price=product.get('price'))

    def _from_document_to_order(self, order):
        orderLines = list(map(self._enrichOrderLines, order.get('orderLines')))

        result_order_lines = [i for i in orderLines if i] 

        return Order(id=str(order.get('_id')), orderLines=result_order_lines, 
            totalAmount=order.get('totalAmount'), customerData=order.get('customerData'))
