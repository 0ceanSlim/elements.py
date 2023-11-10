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
    # Initial connection to list available wallets
    rpc_connection_list_wallets = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )

    wallet_list = rpc_connection_list_wallets.listwallets()

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
                int(input("Enter the number of the wallet to issue an asset from: "))
                - 1
            )

            if 0 <= wallet_index < len(wallet_list):
                wallet_name = wallet_list[wallet_index]
            else:
                print("Invalid wallet selection. Exiting.")
                exit()

    # Connection to the specific wallet
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}/wallet/{wallet_name}"
    )

    # Asset issuance parameters
    asset_quantity = input("Enter the quantity of the asset to issue: ")
    reissuance_tokens = input("Enter the number of reissuance tokens: ")

    # Additional asset details
    asset_name = input("Enter the asset name: ")
    asset_ticker = input("Enter the asset ticker symbol: ")
    asset_divisibility = int(input("Enter the divisibility of the asset: "))
    asset_issuer = input("Enter the issuer address: ")
    asset_total_tokens = input("Enter the total tokens: ")
    asset_expiry = input("Enter the asset expiry date (YYYY-MM-DD): ")
    asset_minimum_amount = input("Enter the minimum amount: ")
    is_open_asset = input("Is the asset open? (yes/no): ").lower() == "yes"

    # Issue the asset and capture the issuance result
    issuance_result = rpc_connection.issueasset(
        asset_quantity,
        reissuance_tokens,
        True,  # Blind issuance
        "0000...0000",  # Contract hash
        asset_name,
        asset_ticker,
        asset_divisibility,
        asset_issuer,
        asset_total_tokens,
        asset_expiry,
        asset_minimum_amount,
        is_open_asset,
    )

    print("Asset issuance result:", issuance_result)

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
