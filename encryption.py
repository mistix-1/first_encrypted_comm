from flask import Flask, request, jsonify

app = Flask(__name__)

# Store messages in-memory (simple lists)
messages_for_bob = []
messages_for_alice = []

@app.route('/send_from_alice', methods=['POST'])
def send_from_alice():
    data = request.json
    # Data should contain 'payload', 'iteration', 'length', 'tag'
    messages_for_bob.append(data)
    return jsonify({"status": "Message from Alice received!"})

@app.route('/get_for_bob', methods=['GET'])
def get_for_bob():
    return jsonify({"messages": messages_for_bob})

@app.route('/send_from_bob', methods=['POST'])
def send_from_bob():
    data = request.json
    messages_for_alice.append(data)
    return jsonify({"status": "Message from Bob received!"})

@app.route('/get_for_alice', methods=['GET'])
def get_for_alice():
    return jsonify({"messages": messages_for_alice})

if __name__ == "__main__":
    app.run(debug=True)
