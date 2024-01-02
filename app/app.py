from flask import Flask, request, jsonify, render_template

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

from src import create_wallet, connect_to_node

app = Flask(__name__, static_folder="static")

@app.route("/")
def show_wallet_form():
    return render_template("index.html")

# Route to get the current RPC configuration
@app.route("/get_rpc_config", methods=["GET"])
def get_rpc_config():
    return jsonify(
        {
            "rpcHost": request.cookies.get("rpcHost"),
            "rpcPort": request.cookies.get("rpcPort"),
            "rpcUser": request.cookies.get("rpcUser"),
            "rpcPassword": request.cookies.get("rpcPassword"),
        }
    )


# Route to update the RPC configuration
@app.route("/update_rpc_config", methods=["POST"])
def update_rpc_config():
    try:
        # Extract RPC config from the POST request
        rpc_host = request.form["rpcHost"]
        rpc_port = request.form["rpcPort"]
        rpc_user = request.form["rpcUser"]
        rpc_password = request.form["rpcPassword"]

        # Update localStorage with the new values
        response = jsonify({"message": "RPC configuration updated successfully."})
        response.set_cookie("rpcHost", value=rpc_host)
        response.set_cookie("rpcPort", value=rpc_port)
        response.set_cookie("rpcUser", value=rpc_user)
        response.set_cookie("rpcPassword", value=rpc_password)
        return response
    except Exception as e:
        return jsonify({"message": f"Error updating RPC configuration: {str(e)}"})

@app.route("/create_wallet", methods=["POST"])
def handle_create_wallet():
    wallet_name = request.form["walletName"]
    
    # Retrieve RPC credentials from localStorage (cookies)
    rpc_host = request.cookies.get("rpcHost")
    rpc_port = request.cookies.get("rpcPort")
    rpc_user = request.cookies.get("rpcUser")
    rpc_password = request.cookies.get("rpcPassword")

    # Create wallet using retrieved RPC credentials
    result = create_wallet(wallet_name, rpc_host, rpc_port, rpc_user, rpc_password)
    
    return jsonify({"message": result})


# Fetch wallets route using RPC credentials from localStorage
@app.route("/wallets", methods=["GET"])
def list_wallets():
    try:
        # Retrieve RPC credentials from localStorage (cookies)
        rpc_host = request.cookies.get("rpcHost")
        rpc_port = request.cookies.get("rpcPort")
        rpc_user = request.cookies.get("rpcUser")
        rpc_password = request.cookies.get("rpcPassword")

        # Establish connection to Bitcoin node using RPC credentials
        rpc_connection = connect_to_node(rpc_host, rpc_port, rpc_user, rpc_password)

        # Fetch wallet list using the established connection
        wallet_list = rpc_connection.listwallets()
        return jsonify({"wallets": wallet_list})  # Return JSON response with wallets
    except JSONRPCException as json_exception:
        error_message = "A JSON RPC Exception occurred: " + str(json_exception)
        return jsonify({"error": error_message})  # Return JSON error response
    except Exception as general_exception:
        error_message = "An Exception occurred: " + str(general_exception)
        return jsonify({"error": error_message})  # Return JSON error response

@app.route("/set_active_wallet", methods=["POST"])
def set_active_wallet():
    wallet_name = request.form["walletName"]
    return jsonify({"message": f"Active wallet set to '{wallet_name}'."})

active_wallet = {}  # Store active wallets in memory

@app.route("/delete_active_wallet", methods=["DELETE"])
def delete_active_wallet():
    global active_wallet  # Assuming active_wallet is a global variable

    try:
        # Retrieve the active wallet from the request data
        wallet_name = request.json.get("walletName")

        # Retrieve RPC credentials from localStorage (cookies)
        rpc_host = request.cookies.get("rpcHost")
        rpc_port = request.cookies.get("rpcPort")
        rpc_user = request.cookies.get("rpcUser")
        rpc_password = request.cookies.get("rpcPassword")

        # Establish a connection to the Bitcoin node using RPC credentials
        rpc_connection = AuthServiceProxy(
            f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
        )

        # Unload the specified wallet from the node
        rpc_connection.unloadwallet(wallet_name)

        # Remove the wallet from active_wallet (if it's stored there)
        if wallet_name in active_wallet:
            del active_wallet[wallet_name]

        return jsonify({"message": f"Deleted active wallet '{wallet_name}'"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)