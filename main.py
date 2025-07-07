from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server AI XAU/USD Aktif"

@app.route("/api/signal")
def signal():
    return jsonify({
        "message": "Sinyal AI XAU/USD - Test"
    })
