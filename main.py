from flask import Flask, jsonify, render_template, request
from forms import DataTriggerForm
import os
import json
from web3 import Web3
import requests
from wordcloud import WordCloud

wc = WordCloud()

ALCHEMY_KEY = 'FxyLBv3WXSLLlt09llm7JjMnRWrxYCZB'
w3 = Web3(Web3.HTTPProvider('https://eth-mainnet.alchemyapi.io/v2/'+ALCHEMY_KEY))

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/server', methods=['GET', 'POST'])
def server():

	if request.method == 'POST':

		result = request.data
		print(result)
		result = json.loads(result)

		for i in range(len(result["activity"])):
			from_address = (result["activity"][i]["fromAddress"])

			f = open("demo.txt", "a")
			f.write(str(from_address)+" ")
			f.close()

		# Read the whole text.
		text = open('demo.txt').read()
		print(text)
		wc = WordCloud(background_color="white", max_words=2000)

		# generate word cloud
		wc.generate(text)
		svg_text = wc.to_svg()

		return (svg_text)


	if request.method == 'GET':
		id = request.args.get('id')
		print(id)

		return(id)

	#return render_template('index.html', form=form, bal=balance, block_num=block_num, total_burn=total_burn)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
