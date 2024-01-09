from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# # Configure MongoDB client
# client = MongoClient("mongodb+srv://admin@mygitdb.v0gnkoy.mongodb.net/")
# db = client.Meeting_automation
# collection = db.meeting_link

@app.route('/postdata', methods=['POST'])
def post_data():
    # Parse data from request
    data = request.data.decode('utf-8')
    print(data)

    # Save data to MongoDB
    # collection.insert_one(data)

    # Send response
    return jsonify({'message': 'information noted'})

if __name__ == '__main__':
    app.run(debug=True)
