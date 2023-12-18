from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from util.rpcHandler import read_rpc_config, create_rpc_connection
from mnemonic import Mnemonic

# Read the RPC configuration from the configuration file
rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()

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

        # Generate HD seed
        mnemonic = Mnemonic("english")
        seed_words = mnemonic.generate(256)  # 256 bits entropy for BIP39
        print("Write down these seed words:")
        print(seed_words)

        # You might want to save or display these seed words securely for the user

    else:
        print(f"Wallet '{wallet_name}' already exists.")

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
