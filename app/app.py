from flask import Flask, request, jsonify, render_template
from ..src import create_wallet, generate_seed

app = Flask(__name__)

@app.route('/')
def show_wallet_form():
    return render_template('index.html')

@app.route('/create_wallet', methods=['POST'])
def handle_create_wallet():
    wallet_name = request.form['walletName']
    result = create_wallet(wallet_name)
    return jsonify({'message': result})

@app.route('/generate_seed', methods=['POST'])
def handle_generate_seed():
    seed_length = request.form['seedLength']
    result = generate_seed(seed_length)
    return jsonify({'seed': result})

if __name__ == "__main__":
    app.run(debug=True)