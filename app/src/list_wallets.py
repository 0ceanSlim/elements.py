from flask import render_template

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from src.read_rpc_config import read_rpc_config


def list_wallets():
    try:
        rpc_host, rpc_port, rpc_user, rpc_password = read_rpc_config()

        rpc_connection = AuthServiceProxy(
            f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
        )

        wallet_list = rpc_connection.listwallets()

        return render_template("index.html", wallets=wallet_list)

    except JSONRPCException as json_exception:
        error_message = "A JSON RPC Exception occurred: " + str(json_exception)
        return render_template("error.html", error=error_message)

    except Exception as general_exception:
        error_message = "An Exception occurred: " + str(general_exception)
        return render_template("error.html", error=error_message)
