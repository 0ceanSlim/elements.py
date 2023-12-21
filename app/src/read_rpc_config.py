import json

def read_rpc_config(filename="rpc_config.json"):
    with open(filename, "r") as config_file:
        config = json.load(config_file)

    rpc_host = config["rpc_host"]
    rpc_port = config["rpc_port"]
    rpc_user = config["rpc_user"]
    rpc_password = config["rpc_password"]

    return rpc_host, rpc_port, rpc_user, rpc_password