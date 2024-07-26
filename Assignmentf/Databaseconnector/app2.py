#How would you create a RESTful API endpoint in Flask that returns JSON data?
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

# Define Routes and Return JSON Data

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [user for user in users if user['id'] != id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run()