from flask import Flask, jsonify, request
from sale_model import SaleItem
from sale_service import SaleService

app = Flask(__name__)
service = SaleService()

@app.route('/sale', methods=['POST'])
def create_sale():
    data = request.json
    client_id = data.get('client_id')
    items = data.get('items')
    
    sale_items = [SaleItem(product_id=item.get('product_id'), quantity=item.get('quantity')) for item in items]
    sale_id = service.create_sale(client_id, sale_items)
    return jsonify({"sale_id": sale_id}), 201

@app.route('/sale/item/<int:item_id>', methods=['PUT', 'PATCH'])
def update_sale_item_quantity(item_id):
    data = request.json
    quantity = data.get('quantity')
    service.update_sale_item_quantity(item_id, quantity)
    return '', 204

@app.route('/sale/<int:sale_id>/finalize', methods=['PUT', 'PATCH'])
def finalize_sale(sale_id):
    service.finalize_sale(sale_id)
    return '', 204

@app.route('/sale/product/<int:product_id>', methods=['GET'])
def get_sales_by_product(product_id):
    sales = service.get_sales_by_product(product_id)
    return jsonify([sale.__dict__ for sale in sales])

@app.route('/sale/state/<int:state_id>', methods=['GET'])
def get_sales_by_state(state_id):
    sales = service.get_sales_by_state(state_id)
    return jsonify([sale.__dict__ for sale in sales])

@app.route('/sale/<int:sale_id>/cancel', methods=['PUT', 'PATCH'])
def cancel_sale(sale_id):
    service.cancel_sale(sale_id)
    return '', 204

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
