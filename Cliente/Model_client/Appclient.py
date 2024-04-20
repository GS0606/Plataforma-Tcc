from flask import Flask, jsonify, request
from service_client import ClientService

app = Flask(__name__)
controller = ClientService()

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = controller.get_all_clients()
    clients_serializable = [client.__dict__ for client in clients]
    return jsonify(clients_serializable)

@app.route('/clients/<int:id>', methods=['GET'])
def get_client_by_id(id):
    try:
        client = controller.get_client(id)
        client_serializable = client.__dict__
        return jsonify(client_serializable)
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@app.route('/clients', methods=['POST'])
def create_client():
    new_client_data = request.get_json()
    new_client_id = controller.create_client(name=new_client_data['name'], surname=new_client_data['surname'], email=new_client_data['email'], data_nascimento=new_client_data['data_nascimento'])
    return jsonify({"message": "Client created successfully", "client_id": new_client_id}), 201

@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    updated_client_data = request.get_json()
    controller.update_client(client_id=id, name=updated_client_data['name'], surname=updated_client_data['surname'], email=updated_client_data['email'], data_nascimento=updated_client_data['data_nascimento'])
    return jsonify({"message": "Client updated successfully"}), 200

@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    controller.delete_client(client_id=id)
    return jsonify({"message": "Client deleted successfully"}), 200

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
