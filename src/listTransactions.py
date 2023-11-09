from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Read the RPC configuration from the configuration file
with open("rpc_config.json", "r") as config_file:
    config = json.load(config_file)

rpc_host = config["rpc_host"]
rpc_port = config["rpc_port"]
rpc_user = config["rpc_user"]
rpc_password = config["rpc_password"]

# List available wallets
try:
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )

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
                int(input("Enter the number of the wallet to check transactions for: "))
                - 1
            )

            if 0 <= wallet_index < len(wallet_list):
                wallet_name = wallet_list[wallet_index]
            else:
                print("Invalid wallet selection. Exiting.")
                exit()

    # Now that wallet_name is defined, proceed with the RPC connection
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}/wallet/{wallet_name}"
    )

    # Get the list of transactions for the selected wallet
    transactions = rpc_connection.listtransactions()

    if not transactions:
        print(f"No transactions found for wallet '{wallet_name}'.")
    else:
        print(f"Transactions for wallet '{wallet_name}':")
        for transaction in transactions:
            print(f"Transaction ID: {transaction['txid']}")
            print(f"Category: {transaction['category']}")
            print(f"Amount: {transaction['amount']} {transaction['asset']}")
            print(f"Confirmations: {transaction['confirmations']}\n")

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
