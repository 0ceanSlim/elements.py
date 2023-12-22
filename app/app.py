from flask import Flask, request, jsonify, render_template
import json

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from src import create_wallet, read_rpc_config, generate_seed, list_wallets

app = Flask(__name__, static_folder="static")


@app.route("/")
def show_wallet_form():
    return render_template("index.html")


@app.route("/create_wallet", methods=["POST"])
def handle_create_wallet():
    wallet_name = request.form["walletName"]
    result = create_wallet(wallet_name)
    return jsonify({"message": result})


@app.route("/generate_seed", methods=["POST"])
def handle_generate_seed():
    seed_length = request.form["seedLength"]
    result = generate_seed(seed_length)
    return jsonify({"seed": result})


@app.route("/wallets", methods=["GET"])
def list_wallets():
    try:
        rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()
        rpc_connection = AuthServiceProxy(
            f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
        )
        wallet_list = rpc_connection.listwallets()
        return jsonify({"wallets": wallet_list})  # Return JSON response with wallets
    except JSONRPCException as json_exception:
        error_message = "A JSON RPC Exception occurred: " + str(json_exception)
        return jsonify({"error": error_message})  # Return JSON error response
    except Exception as general_exception:
        error_message = "An Exception occurred: " + str(general_exception)
        return jsonify({"error": error_message})  # Return JSON error response


# Route to get the current RPC configuration
@app.route("/get_rpc_config", methods=["GET"])
def get_rpc_config():
    rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()
    return jsonify(
        {
            "rpcHost": rpc_host,
            "rpcPort": rpc_port,
            "rpcUser": rpc_user,
            "rpcPassword": rpc_password,
        }
    )


# Route to update the RPC configuration
@app.route("/update_rpc_config", methods=["POST"])
def update_rpc_config():
    rpc_host = request.form["rpcHost"]
    rpc_port = request.form["rpcPort"]
    rpc_user = request.form["rpcUser"]
    rpc_password = request.form["rpcPassword"]

    # Update the RPC configuration file or database with the new values
    # You may want to perform validation or error handling here

    # For demonstration purposes, let's update the configuration and return success
    try:
        with open("rpc_config.json", "w") as config_file:
            config = {
                "rpc_host": rpc_host,
                "rpc_port": rpc_port,
                "rpc_user": rpc_user,
                "rpc_password": rpc_password,
            }
            json.dump(config, config_file)
        return jsonify({"message": "RPC configuration updated successfully."})
    except Exception as e:
        return jsonify({"message": f"Error updating RPC configuration: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
