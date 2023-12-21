from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from util.rpcHandler import read_rpc_config, create_rpc_connection

# Read the RPC configuration from the configuration file
rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()

try:
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )

    # List available wallets
    wallet_list = rpc_connection.listwallets()

    if wallet_list:
        print("Available wallets:")
        for wallet in wallet_list:
            print(wallet)
    else:
        print("No wallets found.")

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
