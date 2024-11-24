from flask import Flask, jsonify

app = Flask(__name__)

# Mock database to store messages
mock_db = {}

@app.route('/')
def is_alive():
    return jsonify('live')

@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    print(f"msg_post_api with message: {msg}")
    # Simulate storing the message in a mock DB (in-memory dictionary)
    msg_id = len(mock_db) + 1  # Generate a simple ID based on the current length of the mock DB
    mock_db[msg_id] = msg  # Store the message
    return jsonify({'msg_id': msg_id})

@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")
    # Retrieve message from the mock DB
    msg = mock_db.get(msg_id, None)  # None if the ID doesn't exist
    if msg is None:
        return jsonify({'error': 'Message not found'}), 404
    return jsonify({'msg': msg})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  
