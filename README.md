# Elements Node Python RPC Tools

This repository contains a collection of simple Python tools for interacting with an Elements node using RPC credentials. These scripts allow you to perform various tasks such as checking balances, sending assets, creating wallets, and more.


## Setup

Clone this repository to your local machine:

```bash
git clone https://happytavern.co/oceanslim/elements.py.git
cd elements.py
```

## Usage

### Windows
Download the latest cli.exe from the releases page of this repository and place it in the cli folder before running it. The exe will walk you through all the necessay steps to begin using the cli and when all requirements are met, the cli will load with initial instructions. 

If you are on Linux or MacOS, you will need python installed before you can run cli.py
You can download Python [Here](https://www.python.org/downloads/)

### Running with Python (any system)
**From the cli directory** run:
```bash 
python cli.py
```

## Flask App Development
First install the requirements with 
```bash
pip install -r requirements.txt
```
Then from the root directory, run:
```bash
python -m flask --app .\app\app.py run
``` 
This will start the app @ http://127.0.0.1:5000

***
Tailwind CSS is used to style the app.    
To update the style output, you need to run 
```bash
 tailwindcss -i app/static/style/input.css -o app/static/style/output.css --watch
 ```

## License

This repository is provided under the MIT License. Feel free to use, modify, and distribute these scripts as needed. Contributions and improvements are welcome. ❤️    
See the [LICENSE](LICENSE) file for details.