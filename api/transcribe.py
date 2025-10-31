from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/transcribe", methods=["GET"])
def hello():
    return jsonify({"status": "ok", "message": "Voice Studio API ready!"})

