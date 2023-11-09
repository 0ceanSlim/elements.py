from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json

# Read the RPC configuration from the configuration file
with open("rpc_config.json", "r") as config_file:
    config = json.load(config_file)

rpc_host = config["rpc_host"]
rpc_port = config["rpc_port"]
rpc_user = config["rpc_user"]
rpc_password = config["rpc_password"]

# Asset issuance parameters
asset_quantity = 100
asset_name = "MyAsset"  # Uncomment and specify the asset name
asset_ticker = "MA"  # Uncomment and specify the asset ticker symbol
asset_divisibility = 8  # Uncomment and specify the divisibility
# asset_issuer = "issuer_address"  # Uncomment and specify the issuer address
# asset_total_tokens = 1000  # Uncomment and specify the total tokens
# asset_expiry = "YYYY-MM-DD"  # Uncomment and specify the asset expiry date
# asset_minimum_amount = 0.00000001  # Uncomment and specify the minimum amount
# reissuance_tokens = 1  # Uncomment and specify the number of reissuance tokens
is_open_asset = True  # Uncomment to specify if the asset is open

try:
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )

    # Construct the issueasset command with the specified options
    issue_command = f"issueasset {asset_quantity}"

    # Uncomment and customize the options in the issue command as needed
    # if asset_name:
    #     issue_command += f' "{asset_name}"'
    # if asset_ticker:
    #     issue_command += f' "{asset_ticker}"'
    # if asset_divisibility is not None:
    #     issue_command += f' {asset_divisibility}'
    # if asset_issuer:
    #     issue_command += f' "{asset_issuer}"'
    # if asset_total_tokens is not None:
    #     issue_command += f' {asset_total_tokens}'
    # if asset_expiry:
    #     issue_command += f' "{asset_expiry}"'
    # if asset_minimum_amount is not None:
    #     issue_command += f' {asset_minimum_amount}'
    # if reissuance_tokens is not None:
    #     issue_command += f' {reissuance_tokens}'
    # if is_open_asset is not None:
    #     issue_command += f' {"open" if is_open_asset else "confidential"}'

    issuance_result = rpc_connection.help(issue_command)
    print("Asset issuance result:", issuance_result)

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
