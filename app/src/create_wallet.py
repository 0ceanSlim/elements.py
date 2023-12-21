from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from src.read_rpc_config import read_rpc_config

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