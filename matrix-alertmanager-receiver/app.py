from flask import Flask, request, jsonify
import requests
import os
import threading

app = Flask(__name__)

MATRIX_HOMESERVER = os.getenv("MATRIX_HOMESERVER_URL")
ACCESS_TOKEN = os.getenv("MATRIX_ACCESS_TOKEN")
ROOM_ID = os.getenv("MATRIX_ROOM_ID")
SECRET = os.getenv("APP_ALERTMANAGER_SECRET")

RETENTION_SIZE = 100
sent_messages = []

def redact_message(event_id):
    url = f"{MATRIX_HOMESERVER}/_matrix/client/v3/rooms/{ROOM_ID}/redact/{event_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    payload = {"reason": "Size-based retention cleanup"}
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code == 200:
        print(f"Message {event_id} redacted successfully")
    else:
        print(f"Failed to redact message {event_id}: {r.text}")

def send_to_matrix(message):
    url = f"{MATRIX_HOMESERVER}/_matrix/client/v3/rooms/{ROOM_ID}/send/m.room.message"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    payload = {
        "msgtype": "m.text",
        "body": message
    }
    r = requests.post(url, json=payload, headers=headers)
    r.raise_for_status()
    resp = r.json()

    event_id = resp["event_id"]
    sent_messages.append(event_id)

    while len(sent_messages) > RETENTION_SIZE:
        oldest_event_id = sent_messages.pop(0)
        threading.Thread(target=redact_message, args=(oldest_event_id,)).start()

    return resp

@app.route("/alert", methods=["POST"])
def alert():
    if SECRET and request.headers.get("Authorization") != f"Bearer {SECRET}":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    alerts = data.get("alerts", [])

    for alert in alerts:
        status = alert.get("status")
        labels = alert.get("labels", {})
        annotations = alert.get("annotations", {})
        name = labels.get("alertname", "NoName")
        description = annotations.get("description", "")
        message = f"🚨 [{status.upper()}] {name}: {description}"
        send_to_matrix(message)

    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("APP_PORT", 3000)))
