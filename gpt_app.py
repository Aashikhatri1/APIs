from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# # Configure MongoDB client
# client = MongoClient("mongodb://localhost:27017/")
# db = client.your_database_name
# collection = db.your_collection_name

@app.route('/postdata', methods=['POST'])
def post_data():
    # Parse data from request
    data = request.data.decode('utf-8')

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

if __name__ == '__main__':
    app.run(debug=True)
