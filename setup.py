import os
import json
import subprocess
import sys


# Check if Python is installed
def check_python_installation():
    try:
        python_version = subprocess.check_output(
            ["python", "--version"], stderr=subprocess.STDOUT, universal_newlines=True
        )
        print(f"Python is already installed ({python_version})")
        return True
    except FileNotFoundError:
        return False


# Install Python if not installed
def install_python():
    print("Python is not installed. Please download and install it from:")
    print("https://www.python.org/downloads/")
    sys.exit(1)


# Check if rpc_config.json exists
def check_rpc_config():
    if os.path.exists("rpc_config.json"):
        return True
    return False


# Prompt the user for RPC config details
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


def main():
    if not check_python_installation():
        install_python()
    else:
        # Install requirements
        subprocess.run(["pip", "install", "-r", "requirements.txt"])

    if not check_rpc_config():
        print("RPC config file not found.")
        user_input = input(
            "Do you have credentials for your Elements node RPC (yes/no)? "
        ).lower()
        if user_input in ["no", "n", "No", "N"]:
            print(
                "Please follow the instructions to set up an Elements node: [https://docs.liquid.net/docs/building-on-liquid]"
            )
            sys.exit(1)
        elif user_input in ["yes", "y", "Yes", "Y"]:
            get_rpc_config()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    else:
        print("You are ready to proceed.")


if __name__ == "__main__":
    main()
