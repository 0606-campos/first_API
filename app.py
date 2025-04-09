from flask import Flask, jsonify

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


app.run(port=4000)