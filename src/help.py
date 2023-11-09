def help():
    print("\nAvailable Commands:")
    print("createWallet - Create a Wallet on your Elements Node")
    print(
        "getNewAddress - Prompts for wallet selection, then generates a new receiving address"
    )
    print(
        "listTransactions - Prompts for wallet selection, then lists all the transactions made in the selected wallet"
    )
    print(
        "listUnspent - Prompts for wallet selection, then lists the selected wallet's asset balances"
    )
    print("listWallets - Lists all the Wallets that exist on your Elements Node")
    print(
        "sendToAddress - Create and sign a new transaction to send assets from the selected Wallet"
    )
    print("help - Display available commands")
    print("exit - Quit the program\n")
