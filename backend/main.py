from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def is_alive():
    return jsonify('live')


@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    print(f"msg_post_api with message: {msg}")
    # TODO: store msg in DB and return identifier
    return jsonify({'msg_id': msg_id})


@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")
    # TODO: get msg from DB and return it
    return jsonify({'msg': msg})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
