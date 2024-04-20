from flask import Flask, jsonify, request
from service_product import ProductService

app = Flask(__name__)
controller = ProductService()

@app.route('/products', methods=['GET'])
def get_products():
    products = controller.get_all_products()
    products_serializable = [product.__dict__ for product in products]
    return jsonify(products_serializable)

@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id):
    try:
        product = controller.get_product(id)
        product_serializable = product.__dict__
        return jsonify(product_serializable)
    except ValueError as e:
        return jsonify({"message": str(e)}), 404

@app.route('/products', methods=['POST'])
def create_product():
    new_product_data = request.get_json()
    new_product_id = controller.create_product(name=new_product_data['name'], dest=new_product_data['dest'], quantity=new_product_data['quantity'])
    return jsonify({"message": "product created successfully", "product_id": new_product_id}), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    updated_product_data = request.get_json()
    controller.update_product(product_id=id, name=updated_product_data['name'], dest=updated_product_data['dest'], quantity=updated_product_data['quantity'])
    return jsonify({"message": "Product updated successfully"}), 200

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    controller.delete_product(product_id=id)
    return jsonify({"message": "Product deleted successfully"}), 200

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
