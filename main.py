import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server AI XAU/USD Aktif"

@app.route("/api/signal")
def signal():
    return jsonify({
        "message": "Tes sinyal AI XAU/USD aktif"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
