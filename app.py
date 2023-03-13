from flask import Flask 
from flask import request
from pymongo import MongoClient
from bson import ObjectId



client = MongoClient('mongodb://mongo:27017/mydatabase', 27017)
db = client.inventoryDB

app = Flask(__name__) 

@app.route('/')
def hello():
    return 'halo, World!'

@app.route('/equipment', methods=['POST'])
def create_user():
    # Get data from request body
    data = request.json
    # Insert data into MongoDB
    db.equipment.insert_one(data)
    # Return success response
    return {'message': ' created successfully'}

@app.route('/equipment', methods=['GET'])
def get_equipment():
    # Retrieve all equipment from MongoDB
    equipment = list(db.equipment.find())
    if len(equipment)==0:
         return {'no items were found'}
    # Convert ObjectId to string
    for eq in equipment:
        eq['_id'] = str(eq['_id'])
    # Return equipment as JSON
    return {'equipment': equipment}

@app.route('/equipment/all', methods=['GET'])
def get_all_equipment():

    # Retrieve all equipment from MongoDB
    equipment = list(db.equipment.find())
    if len(equipment)==0:
         return {'no items were found'}
    return {'equipment': equipment}

@app.route('/equipment/<id>', methods=['PUT'])
def update_user(id):
    # Get data from request body
    data = request.json
    # Update data in MongoDB
    db.equipment.update_one({'_id': ObjectId(id)}, {'$set': data})
   # Return success response
    return {'message': 'User updated successfully'}


@app.route('/equipment/<id>', methods=['DELETE'])
def delete_user(id):
    # Delete user from MongoDB
    db.equipment.delete_one({'_id': ObjectId(id)})
    # Return success response
    return {'message': ' deleted successfully'}



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
