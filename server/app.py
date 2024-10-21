from flask import Flask, request, jsonify
import pika

app = Flask (__name__)

def conect_rabbit():
    try:
        connection_parameters = pika.ConnectionParameters(
            host="rabbitmq",
            port=5672,
            credentials=pika.PlainCredentials(
                username="guest",
                password="guest"
            )
        )
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        print("Conect in RabbitMQ")
        return connection, channel
    except Exception as e:
        print(f"Failed to connect RabbitMQ: {str(e)}")
        return None, None

@app.route('/notify', methods=['POST'])
def notificar():
    connection, channel = conectar_rabbit()
    if channel == None:
        return jsonify({"error": "Falha ao conectar ao RabbitMQ"}), 500

    channel.queue_declare(queue='data_queue', durable=True)
    mensagem = request.json.get('mensage')

    try:
        channel.basic_publish(
            exchange='',
            routing_key='data_queue',
            body=mensagem,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        connection.close()
        return jsonify({"STATUS": "MENSAGEM ENVIADA", "Mensagem enviada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"STATUS": f"Erro ao enviar a mensagem: {str(e)}"}), 500

@app.route('/use', methods=['GET'])
def use():
    connection, channel = conectar_rabbit()
    if channel == None:
        return jsonify({"error": "Faill to conect RabbitMQ"}), 500

    method_frame, header_frame, body = channel.basic_get(queue='data_queue')

    if method_frame:
        channel.basic_ack(method_frame.delivery_tag)
        mensagem = body.decode('utf-8')
        __fechar_conexao(channel, connection)
        print(f"use mensage: {mensagem}")
        return jsonify({"mensage": mensage}), 200
    else:
        __fechar_conexao(channel, connection)
        return jsonify({"STATUS": "sem mensagem na fila"}), 200

def __close_conection(channel, connection):
    channel.close()
    connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)