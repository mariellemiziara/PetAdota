from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook_notification():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data received"}), 400

    notification_message = data.get("message", "No message provided")
    print(f"Notification received: {notification_message}")

    return jsonify({"status": "Notification received", "message": notification_message}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)