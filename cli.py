import argparse
import sys
import os

def run_script(script_name):
    script_path = os.path.join("src", f"{script_name}.py")
    
    if os.path.exists(script_path):
        print(f"Running {script_name}...")
        os.system(f"python {script_path}")
    else:
        print(f"Error: {script_name} not found!")

def main():
    parser = argparse.ArgumentParser(description="Elements Python Command Line Interfacce")

    parser.add_argument("-createWallet", action="store_true", help="Create a Wallet on your Elements Node")
    parser.add_argument("-newAddress", action="store_true", help="Prompts for wallet selection, then generates a new recieving address")
    #parser.add_argument("-issueAsset", action="store_true", help="This script has not been tested will not prompt for input")
    parser.add_argument("-listTransactions", action="store_true", help="Prompts for wallet selection, then lists all the transactions made in the selected wallet")
    parser.add_argument("-listUnspent", action="store_true", help="Prompts for wallet selection, then lists the selected wallets asset balances")
    parser.add_argument("-listWallets", action="store_true", help="Lists all the Wallets that exist on your Elements Node")
    parser.add_argument("-sendToAddress", action="store_true", help="Create and sign a new transaction to send assets from the selected Wallet")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
    elif args.createWallet:
        run_script("createWallet")
    elif args.newAddress:
        run_script("getNewAddress")
    elif args.listTransactions:
        run_script("listTransactions")
    elif args.listUnspent:
        run_script("listUnspent")
    elif args.listWallets:
        run_script("listWallets")
    elif args.sendToAddress:
        run_script("sendToAddress")
    else:
        print("Error: Invalid command. Use -help for usage information.")

if __name__ == "__main__":
    main()
