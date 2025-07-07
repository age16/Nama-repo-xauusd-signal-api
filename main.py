from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/signal', methods=['GET'])
def get_signal():
    signal = {
        "message": "🤖 AI Signal XAU/USD\n📈 Sinyal: BUY\n💰 Harga: 3310.45\n🎯 TP: 3318.00\n⛔ SL: 3302.00\n🧠 Confidence: 92%"
    }
    return jsonify(signal)
