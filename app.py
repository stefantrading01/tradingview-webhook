from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Webhook TradingView actif"}), 200

@app.route('/webhook', methods=['POST'])
def receive_alert():
    try:
        data = request.json
        
        print(f"\n{'='*50}")
        print(f"ALERTE REÇUE - {datetime.now()}")
        print(f"{'='*50}")
        print(f"Données brutes : {json.dumps(data, indent=2)}")
        print(f"{'='*50}\n")
        
        action = data.get('action', 'N/A')
        symbol = data.get('symbol', 'N/A')
        quantity = data.get('quantity', 'N/A')
        
        print(f"Action : {action}")
        print(f"Symbole : {symbol}")
        print(f"Quantité : {quantity}")
        
        return jsonify({
            "status": "success",
            "message": f"Alerte reçue : {action} {quantity} {symbol}",
            "timestamp": datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        print(f"ERREUR : {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        "status": "Webhook fonctionne",
        "url": "POST sur /webhook avec JSON",
        "exemple": {
            "action": "buy",
            "symbol": "AAPL",
            "quantity": 10
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)