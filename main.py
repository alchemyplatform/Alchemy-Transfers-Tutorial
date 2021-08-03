from flask import Flask, jsonify, render_template, request
from forms import DataTriggerForm
import os
import json
from web3 import Web3
import requests

ALCHEMY_KEY = 'FxyLBv3WXSLLlt09llm7JjMnRWrxYCZB'
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/'+ALCHEMY_KEY))

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/server', methods=['GET', 'POST'])
def server():

    if request.method == 'GET':
        id = request.args.get('id')
        print(id)

        return('NFT ID is: '+string(id))

    #return render_template('index.html', form=form, bal=balance, block_num=block_num, total_burn=total_burn)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
