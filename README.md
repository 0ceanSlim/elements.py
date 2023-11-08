# Elements Node Python RPC Tools

This repository contains a collection of simple Python tools for interacting with an Elements node using RPC credentials. These scripts allow you to perform various tasks such as checking balances, sending assets, creating wallets, and more.

## Prerequisites

Before using these scripts, make sure you have the following prerequisites installed:

- Python (3.x recommended)
- The `python-bitcoinrpc` library for RPC communication.

You can install the required library using pip:

```bash
pip install python-bitcoinrpc
```

## Usage

Clone this repository to your local machine:

```bash
git clone https://happytavern.co/oceanslim/elements.py.git
cd elements.py
```

## Configuration

Create a configuration file, rpc_config.json, and specify your RPC credentials and node information:

```bash
{
  "rpc_host": "xx.x.xx.xxx",
  "rpc_port": 7041,
  "rpc_user": "rpc_user",
  "rpc_password": "rpc_password"
}
```

Modify the scripts to read the RPC configuration from the rpc_config.json file. You can customize the configuration as needed.

## License

This repository is provided under the MIT License. Feel free to use, modify, and distribute these scripts as needed. Contributions and improvements are welcome. ❤️