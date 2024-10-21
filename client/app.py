from flask import Flask, request, jsonify
import requests

app = Flask (__name__)

@app.route('/pay', methods=['POST'])
def pay():
    try:
        response = requests.pos t('http://servidor:5001/notificar', json=request.json)
        return jsonify ({"STATUS": "NOTIFICAÇÃO ENVIDADA", "Notificação enviada com sucesso", "response": response.json()}), 200
    except Exception as e:
        return jsonify ({"STATUS": "NOTIFICAÇÃO NÃO ENVIDADA", "Erro de envio de notificação", "PS": str(e)}), 500

if __name__ == '__main__':
    app.run (host='0.0.0.0', port=5000)