from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from util.rpcHandler import read_rpc_config, create_rpc_connection

# Read the RPC configuration from the configuration file
rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()


def send_to_address():
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
                    int(input("Enter the number of the wallet to send from: ")) - 1
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

        # Prompt the user for the receiving address
        destination_address = input("Enter the receiving address: ")

        if not rpc_connection.validateaddress(destination_address)["isvalid"]:
            print("Invalid destination address. Exiting.")
            exit()

        # Get the asset name you want to send
        asset_name = input("Enter the asset name (e.g., demoasset): ")

        # Get the amount to send
        amount = float(input(f"Enter the amount of {asset_name} to send: "))

        # Additional options
        comment = input("Enter a comment for the transaction (optional): ")
        comment_to = input("Enter a comment for the recipient (optional): ")
        subtract_fee_from_amount = (
            input("Subtract fee from amount? (true/false, optional): ").lower()
            == "true"
        )
        replaceable = (
            input("Enable BIP125 replaceable? (true/false, optional): ").lower()
            == "true"
        )
        conf_target = int(
            input("Enter confirmation target in blocks (optional): ") or 0
        )
        estimate_mode = (
            input("Enter fee estimate mode (unset/economical/conservative, optional): ")
            or "unset"
        )
        avoid_reuse = (
            input(
                "Avoid spending from dirty addresses? (true/false, optional): "
            ).lower()
            == "true"
        )
        asset_label = (
            input("Enter hex asset id or asset label for balance (optional): ") or None
        )
        ignore_blind_fail = (
            input("Ignore blinding failure? (true/false, optional): ").lower() == "true"
        )
        fee_rate = float(input("Enter fee rate in sat/vB (optional): ") or 0)
        verbose = (
            input("Enable verbose mode? (true/false, optional): ").lower() == "true"
        )

        # Build the transaction
        tx_result = rpc_connection.sendtoaddress(
            destination_address,
            amount,
            comment,
            comment_to,
            subtract_fee_from_amount,
            replaceable,
            conf_target,
            estimate_mode,
            avoid_reuse,
            asset_label,
            ignore_blind_fail,
            fee_rate,
            verbose,
        )

        if verbose:
            print("Transaction Details:")
            print(tx_result)
        else:
            print(f"Transaction sent. Transaction ID: {tx_result}")

    except JSONRPCException as json_exception:
        print("A JSON RPC Exception occurred: " + str(json_exception))
    except Exception as general_exception:
        print("An Exception occurred: " + str(general_exception))


if __name__ == "__main__":
    # Retry the operation up to 3 times
    for _ in range(3):
        try:
            send_to_address()
            break  # Break out of the loop if successful
        except JSONRPCException as e:
            print(f"Error: {e}. Retrying...")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Retrying...")
