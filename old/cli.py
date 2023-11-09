import os

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
