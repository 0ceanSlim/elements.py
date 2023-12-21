# get_blockchain_info.py
from util.rpcHandler import read_rpc_config, create_rpc_connection

def get_blockchain_info():
    # Read the RPC configuration from the configuration file
    rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()

    try:
        # Create an RPC connection
        rpc_connection = create_rpc_connection(rpc_host, rpc_port, rpc_user, rpc_password)

        # Get blockchain info
        blockchain_info = rpc_connection.getblockchaininfo()

        # Print the blockchain info
        print("Blockchain Info:")
        print("Chain:", blockchain_info.get("chain"))
        print("Blocks:", blockchain_info.get("blocks"))
        print("Headers:", blockchain_info.get("headers"))
        print("Best Block Hash:", blockchain_info.get("bestblockhash"))
        
        # Check if the 'difficulty' field is present before printing
        if 'difficulty' in blockchain_info:
            print("Difficulty:", blockchain_info["difficulty"])
        else:
            print("Difficulty information not available.")

        print("Median Time:", blockchain_info.get("mediantime"))
        print("Verification Progress:", blockchain_info.get("verificationprogress"))
        print("Initial Block Download:", blockchain_info.get("initialblockdownload"))
        print("Chainwork:", blockchain_info.get("chainwork"))
        print("Size on Disk:", blockchain_info.get("size_on_disk"))
        print("Pruned:", blockchain_info.get("pruned"))
        # Add more fields as needed

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    get_blockchain_info()
