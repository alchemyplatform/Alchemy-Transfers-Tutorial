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


@app.route('/', methods=['GET', 'POST'])
def refresh():

    if request.method == 'GET':
        print(request.data)

        return(request.data)

    #return render_template('index.html', form=form, bal=balance, block_num=block_num, total_burn=total_burn)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
