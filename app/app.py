from flask import Flask, request, jsonify, render_template
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
#from ..src.util.rpcHandler import read_rpc_config
from mnemonic import Mnemonic
#from ..src import create_wallet, generate_seed
import json

app = Flask(__name__)

def read_rpc_config(filename="../rpc_config.json"):
    with open(filename, "r") as config_file:
        config = json.load(config_file)

    rpc_host = config["rpc_host"]
    rpc_port = config["rpc_port"]
    rpc_user = config["rpc_user"]
    rpc_password = config["rpc_password"]

    return rpc_host, rpc_port, rpc_user, rpc_password

def create_rpc_connection(rpc_host, rpc_port, rpc_user, rpc_password):
    rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    return AuthServiceProxy(rpc_url)


# Function to create a wallet
def create_wallet(wallet_name):
    try:
        rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()
        rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")

        wallet_info = rpc_connection.listwallets()

        if wallet_name not in wallet_info:
            rpc_connection.createwallet(wallet_name)
            return f"Wallet '{wallet_name}' created successfully."
        else:
            return f"Wallet '{wallet_name}' already exists."
    except JSONRPCException as json_exception:
        return "A JSON RPC Exception occurred: " + str(json_exception)
    except Exception as general_exception:
        return "An Exception occurred: " + str(general_exception)

# Function to generate seed based on seed length
def generate_seed(seed_length):
    try:
        if seed_length == "12" or seed_length == "24":
            entropy_bits = 128 if seed_length == "12" else 256
            mnemonic = Mnemonic("english")
            seed_words = mnemonic.generate(entropy_bits)
            return seed_words
        else:
            return "Invalid choice. Please choose 12 or 24."
    except Exception as e:
        return "An error occurred: " + str(e)


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


# Route to get the current RPC configuration
@app.route('/get_rpc_config', methods=['GET'])
def get_rpc_config():
    rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()
    return jsonify({'rpcHost': rpc_host, 'rpcPort': rpc_port, 'rpcUser': rpc_user, 'rpcPassword': rpc_password})

# Route to update the RPC configuration
@app.route('/update_rpc_config', methods=['POST'])
def update_rpc_config():
    rpc_host = request.form['rpcHost']
    rpc_port = request.form['rpcPort']
    rpc_user = request.form['rpcUser']
    rpc_password = request.form['rpcPassword']

    # Update the RPC configuration file or database with the new values
    # You may want to perform validation or error handling here

    # For demonstration purposes, let's update the configuration and return success
    try:
        with open("../rpc_config.json", "w") as config_file:
            config = {
                "rpc_host": rpc_host,
                "rpc_port": rpc_port,
                "rpc_user": rpc_user,
                "rpc_password": rpc_password
            }
            json.dump(config, config_file)
        return jsonify({'message': 'RPC configuration updated successfully.'})
    except Exception as e:
        return jsonify({'message': f'Error updating RPC configuration: {str(e)}'})


if __name__ == "__main__":
    app.run(debug=True)