from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from util.rpcHandler import read_rpc_config
from mnemonic import Mnemonic

def create_wallet(wallet_name):
    rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()

    try:
        rpc_connection = AuthServiceProxy(
            f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
        )

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

def generate_seed(seed_length):
    try:
        if seed_length == '12' or seed_length == '24':
            entropy_bits = 128 if seed_length == '12' else 256
            mnemonic = Mnemonic("english")
            seed_words = mnemonic.generate(entropy_bits)
            return seed_words
        else:
            return "Invalid choice. Please choose 12 or 24."
    except Exception as e:
        return "An error occurred while generating the seed phrase: " + str(e)
