from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import json
import hashlib
from getpass import getpass

def get_rpc_credentials_from_file(filename='rpc_config.json'):
    with open(filename, 'r') as config_file:
        config = json.load(config_file)

    rpc_host = config['rpc_host']
    rpc_port = config['rpc_port']
    rpc_user = config['rpc_user']
    rpc_password = config['rpc_password']

    return rpc_host, rpc_port, rpc_user, rpc_password

def generate_contract():
    name = input("Enter the asset name: ")
    ticker = input("Enter the asset ticker: ")
    entity_domain = input("Enter the entity domain: ")
    precision = int(input("Enter the precision (default is 0): ") or 0)

    contract = {
        'version': 0,
        'issuer_pubkey': '',  # Placeholder for the actual pubkey (to be filled later)
        'name': name,
        'ticker': ticker,
        'entity': {'domain': entity_domain},
        'precision': precision
    }

    # Calculate contract hash
    contract_json = json.dumps(contract, separators=(',', ':'), sort_keys=True)
    contract_hash = hashlib.sha256(contract_json.encode('ascii')).hexdigest()
    contract['issuer_pubkey'] = input("Enter the issuer pubkey: ")

    return contract, contract_hash

def prompt_for_additional_options():
    additional_options = input("Do you want to specify additional options for asset issuance? (yes/no): ").lower()
    return additional_options == "yes"

def issue_and_register_asset(rpc_connection, contract, contract_hash):
    # Issue asset
    asset_quantity = input("Enter the quantity of the asset to issue: ")
    reissuance_tokens = input("Enter the number of reissuance tokens: ")

    try:
        issuance_result = rpc_connection.issueasset(
            asset_quantity,
            reissuance_tokens,
            True,  # Blind issuance
            contract_hash,
            contract['name'],
            contract['ticker'],
            contract['precision'],
            rpc_connection.getnewaddress(),
            "1000000",  # Total tokens
            "2030-01-01",  # Asset expiry date
            "0",  # Minimum amount
            False  # Not an open asset
        )

        print("Asset issuance result:", issuance_result)

        # Register asset
        register_result = rpc_connection.registerasset(issuance_result['txid'])
        print("Asset registration result:", register_result)

    except JSONRPCException as json_exception:
        print("A JSON RPC Exception occurred: " + str(json_exception))
    except Exception as general_exception:
        print("An Exception occurred: " + str(general_exception))

if __name__ == '__main__':
    rpc_host, rpc_port, rpc_user, rpc_password = get_rpc_credentials_from_file()

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

            wallet_index = int(input("Enter the number of the wallet to issue an asset to: ")) - 1

            if 0 <= wallet_index < len(wallet_list):
                wallet_name = wallet_list[wallet_index]
            else:
                print("Invalid wallet selection. Exiting.")
                exit()

        # Connection to the specific wallet
        rpc_connection = AuthServiceProxy(
            f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}/wallet/{wallet_name}"
        )

        try:
            contract, contract_hash = generate_contract()

            if prompt_for_additional_options():
                # Additional options can be added here
                pass

            issue_and_register_asset(rpc_connection, contract, contract_hash)

        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
