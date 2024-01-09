from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# # Configure MongoDB client
# client = MongoClient("mongodb+srv://admin@mygitdb.v0gnkoy.mongodb.net/")
# db = client.Meeting_automation
# collection = db.meeting_link

@app.route('/sales_agent', methods=['POST'])
def sales_agent():
    # Parse data from request
    data = request.data.decode('utf-8')
    print(data)

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

@app.route('/customer_support', methods=['POST'])
def customer_support():
    # Parse data from request
    data = request.data.decode('utf-8')
    print(data)

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

@app.route('/habit_coach', methods=['POST'])
def habit_coach():
    # Parse data from request
    data = request.data.decode('utf-8')
    print(data)

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

@app.route('/PA', methods=['POST'])
def PA():
    # Parse data from request
    data = request.data.decode('utf-8')
    print(data)

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

@app.route('/sales_insights', methods=['POST'])
def sales_insights():
    # Parse data from request
    data = request.data.decode('utf-8')
    print(data)

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

if __name__ == '__main__':
    app.run(debug=True)
