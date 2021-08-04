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

		return ("OK")


	if request.method == 'GET':
		id = request.args.get('id')
		print(id)

		# Read the whole text.
		text = open('demo.txt').read()
		print(text)
		wc = WordCloud(background_color="white", max_words=100)

		# generate word cloud
		wc.generate(text)
		svg_text = wc.to_svg()
		print(svg_text)

		pic = {"name":"Neolastic 0x01","description":"Liquid On-Chain Generative Neo-Plastic Art","image_data":"<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><rect x='0' y='0' width='100' height='100' style='fill:#fac901;stroke-width:3;stroke:black'/><rect x='0' y='100' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='0' y='200' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='100' y='0' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='100' y='100' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='100' y='200' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='200' y='0' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='200' y='100' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/><rect x='200' y='200' width='100' height='100' style='fill:undefined;stroke-width:3;stroke:black'/></svg>","attributes":[{"trait_type":"Yellow Tiles","value":"One"},{"trait_type":"Amount of Colours","value":"1 Colours"}]}

		return (pic)


	#return render_template('index.html', form=form, bal=balance, block_num=block_num, total_burn=total_burn)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
