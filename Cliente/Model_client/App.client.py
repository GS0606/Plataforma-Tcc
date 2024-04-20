from flask import Flask, jsonify, request
from service_client import ClientService

app = Flask(__name__)
service = ClientService()

@app.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    new_client_id = service.create_client(name=data['name'], surname=data['surname'], email=data['email'], data_nascimento=data['data_nascimento'])
    return jsonify({'client_id': new_client_id}), 201

@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = service.get_client(client_id)
    if client:
        return jsonify(client.__dict__)
    else:
        return jsonify({'message': 'Cliente não encontrado'}), 404

@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.json
    service.update_client(client_id=client_id, name=data['name'], surname=data['surname'], email=data['email'], data_nascimento=data['data_nascimento'])
    return jsonify({'message': 'Cliente atualizado com sucesso'}), 200

@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    service.delete_client(client_id)
    return jsonify({'message': 'Cliente deletado com sucesso'}), 200

if __name__ == '__main__':
   app.run(port=5000, host='localhost', debug=True)