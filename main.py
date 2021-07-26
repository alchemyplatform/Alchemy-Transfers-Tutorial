from flask import Flask, jsonify, render_template, request
from forms import DataTriggerForm
import os
import json
from web3 import Web3
import requests

ALCHEMY_KEY = os.environ.get('KEY')
print(ALCHEMY_KEY)
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/'+ALCHEMY_KEY))

# includes the standard ERC20 ABI info
ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501

# configures web3 to point towards the AKITA token address
AKITA_ADDRESS = '0x3301Ee63Fb29F863f2333Bd4466acb46CD8323E6'
GITCOIN_ADDRESS = '0xde21F729137C5Af1b01d73aF1dC21eFfa2B8a0d6'
akita = w3.eth.contract(address=AKITA_ADDRESS, abi=ERC20_ABI)

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


def get_block_num():
    return str(w3.eth.get_block('latest')['number'])

def get_gtc_akita_bal():
    return str(akita.functions.balanceOf(GITCOIN_ADDRESS).call())

def get_total_burn():
    total_burn = requests.post('https://eth-mainnet.alchemyapi.io/v2/'+ALCHEMY_KEY, json={"jsonrpc": "2.0","id": 0,"method": "alchemy_getAssetTransfers","params": [{"fromBlock": "0xC30965","toBlock": "latest","fromAddress": "0xde21F729137C5Af1b01d73aF1dC21eFfa2B8a0d6","toAddress": "0xDead000000000000000000000000000000000d06","contractAddresses": ["0x3301Ee63Fb29F863f2333Bd4466acb46CD8323E6"],"category": ["external","token"]}]})

    json_response = total_burn.json()
    transfer_nums = len(json_response['result']['transfers'])

    burned = 0
    for i in range(transfer_nums):
        burned = burned + json_response['result']['transfers'][i]['value']
    return burned

@app.route('/', methods=['GET', 'POST'])
def refresh():
    #num1 = None
    block_num = get_block_num()
    balance = get_gtc_akita_bal()
    total_burn = get_total_burn()

    form = DataTriggerForm()

    if request.method == 'POST':
        #num1 = form.num1.data
        block_num = get_block_num()
        balance = get_gtc_akita_bal()
        total_burn = get_total_burn()

    return render_template('index.html', form=form, bal=balance, block_num=block_num, total_burn=total_burn)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
