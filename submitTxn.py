from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Read the RPC configuration from the configuration file
with open("rpc_config.json", "r") as config_file:
    config = json.load(config_file)

rpc_host = config["rpc_host"]
rpc_port = config["rpc_port"]
rpc_user = config["rpc_user"]
rpc_password = config["rpc_password"]

try:
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )

    # List available wallets
    wallet_list = rpc_connection.listwallets()

    if not wallet_list:
        print("No wallets found.")
    else:
        if len(wallet_list) == 1:
            # If there's only one wallet, use it
            wallet_name = wallet_list[0]
        else:
            # If multiple wallets exist, prompt the user to select one
            print("Available wallets:")
            for i, wallet in enumerate(wallet_list):
                print(f"{i + 1}. {wallet}")

            wallet_index = (
                int(input("Enter the number of the wallet to send from: ")) - 1
            )

            if 0 <= wallet_index < len(wallet_list):
                wallet_name = wallet_list[wallet_index]
            else:
                print("Invalid wallet selection. Exiting.")
                exit()

        # Prompt the user for the receiving address
        destination_address = input("Enter the receiving address: ")

        if not rpc_connection.validateaddress(destination_address)["isvalid"]:
            print("Invalid destination address. Exiting.")
            exit()

        # Get the asset name you want to send
        asset_name = input("Enter the asset name (e.g., demoasset): ")

        # Get the amount to send
        amount = float(input(f"Enter the amount of {asset_name} to send: "))

        # Send the asset to the destination address
        txid = rpc_connection.sendtoaddress(
            destination_address, amount, asset_name, "", False, True, 1
        )

        print(f"Asset sent. Transaction ID: {txid}")

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
