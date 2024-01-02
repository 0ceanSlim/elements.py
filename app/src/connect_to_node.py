
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Function to establish an RPC connection to the Elements node
def connect_to_node(rpc_host, rpc_port, rpc_user, rpc_password):
    rpc_connection = AuthServiceProxy(
        f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
    )
    return rpc_connection
