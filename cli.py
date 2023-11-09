import os
import json
import subprocess
import sys

def check_python_installation():
    try:
        python_version = subprocess.check_output(
            ["python", "--version"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print(f"Python is already installed ({python_version})")
        return True
    except FileNotFoundError:
        return False

def install_python():
    print("Python is not installed. Please download and install it from:")
    print("https://www.python.org/downloads/")
    input("Press Enter to continue after installing Python...")
    sys.exit(1)

def check_rpc_config():
    if os.path.exists("rpc_config.json"):
        return True
    return False

def get_rpc_config():
    rpc_host = input("Enter the RPC host: ")
    rpc_port = input("Enter the RPC port: ")
    rpc_user = input("Enter the RPC user: ")
    rpc_password = input("Enter the RPC password: ")

    rpc_config = {
        "rpc_host": rpc_host,
        "rpc_port": rpc_port,
        "rpc_user": rpc_user,
        "rpc_password": rpc_password,
    }

    with open("rpc_config.json", "w") as config_file:
        json.dump(rpc_config, config_file)

def run_script(script_name):
    script_path = os.path.join("src", f"{script_name}.py")

    if os.path.exists(script_path):
        print(f"Running {script_name}...")
        os.system(f"python {script_path}")
    else:
        print(f"Error: {script_name} not found!")

def help():
    print("\nAvailable Commands:")
    print("createWallet - Create a Wallet on your Elements Node")
    print("newAddress - Prompts for wallet selection, then generates a new receiving address")
    print("listTransactions - Prompts for wallet selection, then lists all the transactions made in the selected wallet")
    print("listUnspent - Prompts for wallet selection, then lists the selected wallet's asset balances")
    print("listWallets - Lists all the Wallets that exist on your Elements Node")
    print("sendToAddress - Create and sign a new transaction to send assets from the selected Wallet")
    print("help - Display available commands")
    print("exit - Quit the program\n")

def main():
    while not check_python_installation():
        install_python()

    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    while not check_rpc_config():
        print("RPC config file not found.")
        user_input = input(
            "Do you have credentials for your Elements node RPC (yes/no)? "
        ).lower()

        if user_input in ["no", "n"]:
            print(
                "Please follow the instructions to set up an Elements node: [https://docs.liquid.net/docs/building-on-liquid]"
            )
            input("Press Enter to continue after setting up the Elements node...")
        elif user_input in ["yes", "y"]:
            get_rpc_config()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    print("You are ready to proceed.")

    print("\nElements Python Command Line Interface")
    help()

    while True:
        user_input = input("Enter a command: ")

        if user_input.lower() == 'exit':
            break

        if user_input == 'createWallet':
            run_script("createWallet")
        elif user_input == 'newAddress':
            run_script("getNewAddress")
        elif user_input == 'listTransactions':
            run_script("listTransactions")
        elif user_input == 'listUnspent':
            run_script("listUnspent")
        elif user_input == 'listWallets':
            run_script("listWallets")
        elif user_input == 'sendToAddress':
            run_script("sendToAddress")
        elif user_input.lower() == 'help':
            help()
        else:
            print("Error: Invalid command. Use 'help' to list commands.")

if __name__ == "__main__":
    main()
