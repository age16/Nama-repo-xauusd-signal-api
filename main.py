from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Server AI XAU/USD Aktif"

@app.route("/api/signal")
def signal():
    return jsonify({
        "message": (
            "🤖 Sinyal SELL XAU/USD\n"
            "📍 Entry: 3300.41\n"
            "⛔ SL: 3308.41\n"
            "🎯 TP1: 3293.41\n"
            "🎯 TP2: 3281.41\n"
            "📊 RSI: 43.2 – lemah, cenderung bearish\n"
            "📈 MA20: 3300.7, MA50: 3299.5\n"
            "📉 Pattern: Bullish Engulfing (TF 30M)\n"
            "📶 TF: SELL | SELL | SELL\n"
            "🧠 Confidence: 87%\n"
            "🕒 17:00 WIB\n"
            "📰 PS: Sentimen pasar sedang mendukung arah turun berdasarkan berita ekonomi terbaru."
        )
    })
