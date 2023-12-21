from bitcoinlib.wallets import Wallet
from bitcoinlib.mnemonic import Mnemonic

# Generate a 12-word mnemonic
mnemonic = Mnemonic().generate()

# Create a wallet from the mnemonic
wallet = Wallet.create("my_wallet", keys=mnemonic, network='bitcoin')

# Get the first address in the wallet
address = wallet.get_key().address

# Get the private key corresponding to the address
private_key = wallet.get_key().wif

print("Mnemonic:", mnemonic)
print("Address:", address)
print("Private Key:", private_key)

#Mnemonic: myth isolate open accident escape ramp flee fork sport slice crouch dice
#Address: 14tmuAfCv5ndX3WsiWndn4SFaexMGTVwJ1
#Private Key: xprvA2aA6xZnkX4zomNmhtRpLCmS7vzNfyFFev3cW8YQQkdvfnPX2AYREhac46nYFuNhRQxn7LQiTZx5cbYceq3y2Zj7C8pxcqomX9Dt2JEbmk3
#generated with script. test.