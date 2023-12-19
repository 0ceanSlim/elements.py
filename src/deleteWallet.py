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
        for index, wallet in enumerate(wallet_list):
            print(f"{index + 1}. {wallet}")

        # Prompt for wallet selection to delete
        selection = input("Enter the number of the wallet to delete (or 0 to cancel): ")
        if selection.isdigit():
            selection = int(selection)
            if 0 < selection <= len(wallet_list):
                wallet_to_delete = wallet_list[selection - 1]
                confirm_deletion = input(f"Are you sure you want to delete '{wallet_to_delete}'? (yes/no): ")
                if confirm_deletion.lower() == "yes":
                    rpc_connection.unloadwallet(wallet_to_delete)
                    print(f"Wallet '{wallet_to_delete}' has been deleted.")
                else:
                    print("Deletion cancelled.")
            elif selection == 0:
                print("Operation cancelled.")
            else:
                print("Invalid selection.")
        else:
            print("Invalid input.")

    else:
        print("No wallets found.")

except JSONRPCException as json_exception:
    print("A JSON RPC Exception occurred: " + str(json_exception))
except Exception as general_exception:
    print("An Exception occurred: " + str(general_exception))
