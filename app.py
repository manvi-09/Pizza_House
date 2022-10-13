#from crypt import methods
from flask import Flask, jsonify, request
from flask_restful import Api
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_pymongo import PyMongo
from bson import json_util
import json, pika

client=MongoClient("localhost:27017")
db=client.pizza_house

    
app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)
api=Api(app)


@app.route("/welcome", methods = ['GET'])    #1.Welcome API
def Welcome():
    data = "Welcome to Pizza House"        #message to be displayed
    return jsonify({'data': data}),200, {'ContentType': 'application/json'}
    
@app.route("/order", methods = ['POST'])    #2.Accept order API
def accept_order():
        order = request.get_json()               #Example input to API - {"order": ["Pizza1", "Pizza2"]}
        id = db.orders.insert_one(order)         #obtain id after inserting the order to the database 
        if order:
            return jsonify({'order_id': str(id.inserted_id)}), 200, {'ContentType': 'application/json'}       #return the required order id
        else:
            return jsonify({'message': 'No order given..!!'}), 400, {'ContentType': 'application/json'}       #display the message if order not present
        
        
@app.route("/getorders",methods=['GET'])         #3.1 Get order details from the database
def getorders():
    orderss = db.orders.find()
    return json.loads(json_util.dumps([i for i in orderss])), 200, {'ContentType': 'application/json'}
    
@app.route("/getorders/<order_id>",methods=['GET'])
def getorder(order_id):
    if not ObjectId.is_valid(order_id):
        return jsonify({"message":"Invalid order id"}), 400, {'ContentType': 'application/json'}
    order = db.orders.find({'_id':ObjectId(order_id)})
    if not order:
        return jsonify({'message': 'No order found'}), 404, {'ContentType': 'application/json'}
    return dumps(order), 200, {'ContentType': 'application/json'}
    
@app.route('/myorder_queue', methods=['POST'])
def order_queue():
    order=request.get_json()
    if not order:
        return jsonify({'message' : 'No order given..!!'}), 400, {'ContentType': 'application/json'}
    id=db.orders.insert_one(order)
    connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel=connection.channel()
    channel.queue_declare(queue='myorder_queue')
    channel.basic.publish(exchange='',routing_key='myorder_queue',body=str(id.inserted_id))
    connection.close()
    return jsonify({'message':'Your order has been placed successfully','order_id':str(id.inserted_id)}), 200, {'ContentType': 'application/json'}


if __name__ == "__main__":
    app.run(debug=True)