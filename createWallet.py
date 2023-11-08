from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Read the RPC configuration from the configuration file
with open("rpc_config.json", "r") as config_file:
    config = json.load(config_file)

rpc_host = config["rpc_host"]
rpc_port = config["rpc_port"]
rpc_user = config["rpc_user"]
rpc_password = config["rpc_password"]

# Prompt the user for the wallet name
wallet_name = input("Enter the wallet name to create: ")

try:
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )

    # Check if the wallet already exists
    wallet_info = rpc_connection.listwallets()

    # If the wallet doesn't exist, create it
    if wallet_name not in wallet_info:
        rpc_connection.createwallet(wallet_name)
        print(f"Wallet '{wallet_name}' created successfully.")
    else:
        print(f"Wallet '{wallet_name}' already exists.")

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
