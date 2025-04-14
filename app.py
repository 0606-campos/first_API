from flask import Flask, jsonify, request

app = Flask(__name__)

purchase_orders= [
    {
        'id': 1,
        'description': 'Pedido de compra 1',
        'itens': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 19.90
            }
        ]
    }
]


@app.route('/')
def home():
    return("Hello World!")

@app.route('/purchase_orders')
def get_purchse_orders():
    return jsonify(purchase_orders)

@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({'message': 'Pedido do cliente {} não encontrado'.format(id)})

@app.route('/purchase_orders', methods=['POST'])
def create_purchase_order():
    request_data = request.get_json()
    purchase_order = {
        'id': request_data['id'],
        'description': request_data['description'],
        'itens': []
    }

    purchase_orders.append(purchase_order)

    return jsonify(purchase_order)

app.run(port=4000)