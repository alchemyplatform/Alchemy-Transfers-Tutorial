Alchemy Transfers 🔀 Tutorial
============

dApps on Ethereum have grown in complexity, depth, and breadth in the past few years. One missing piece is the efficient querying of historical block information. With standard Ethereum JSON-RPC methods, developers either need to maintain centralized databases containing large swaths of the blockchain history or repeatedly query blocks across long time periods in order to scrap the entire transaction history of a particular address. These 2 options complicates the process in which users like wallet providers supply information such as the history of a particular user's interactions on the blockchain. Without easy access to this information, developers must rely on expensive, slow methodsthat limit the feature set of their apps.

While building historical queries into dApps has traditionally been complicated, time-consuming, and error-prone, Alchemy Transfers allows for developers to query historical wallet activity, token transfers, and other account-driven transactions in a simple package.  

In this tutorial, we’ll look at an example of how, with just a few lines of code, your dApp can integrate the 🔋 power of Alchemy Transfers.
***
For ease of user experience, we configured this particular tutorial to run on Heroku, but you are more than welcome to use other service providers!
***

### Problem Statement: 🐕 ###

Instead of sending burnt tokens to 0xdead, which is recommended for most token burning, creators of Akita Inu (AKITA) and Shiba Inu (SHIBA) chose to gift Vitalik Buterin with large swaths of their dog-themed tokens.  Instead of leaving the meme tokens untouched, Vitalk instead chose to sell tokens in batches to Uniswap, swapping them for ETH and donated both the ETH proceeds and the rest of the tokens that could not be sold to a whole host of charities.  Check out [this article](https://www.theblockcrypto.com/post/104676/vitalik-buterin-donates-more-than-60m-to-charity-after-selling-meme-tokens-including-shiba-inu) for more info.

One of the lucky recipients of this windfall was the [Gitcoin community](https://gitcoin.co/) multisig account.  With the market valuation of the AKITA token transfer at ~$450 million, no single market would be able to absorb a single sale of the tokens, and if the multisig attempted to do so, the price of AKITA would plummet.  As such, the Gitcoin community decided to implement a token “rescue” process that would burn 13 AKITA tokens for every 1 AKITA sold off to the open market.   

Our example dashboard follows along with the story of AKITA and its rescue process by tracking the total number of AKITA tokens held in the Gitcoin multisig and the total number of tokens that have been burnt as part of the rescue contract. The dashboard that we create performs two functions.  Upon refresh of page or user click, the webapp fires off a request to Alchemy, querying the Gitcoin multisig address and the “rescue” smart contract.  After receiving the response, the dashboard parses the JSON object and processes it.  Ultimately, the website frontend displays the processed items.

### 🚀 Launching with Heroku ###

 1. Get the repo!

      * `https://github.com/alchemyplatform/Alchemy-Transfers-Tutorial`

For all Heroku dependent documentation, refer to:
https://devcenter.heroku.com/articles/getting-started-with-nodejs?singlepage=true 
for more detailed instructions.  The Heroku instructions included below are abridged.

 2. Install Heroku-CLI and verify/install dependencies.

      * Download Heroku-CLI based on your OS [https://devcenter.heroku.com/articles/heroku-cli]
      * After installation, open your terminal and run `heroku login`; follow the commands that follow to login to your Heroku account.  If you don't have a Heroku account, you can [sign up for one](https://dashboard.heroku.com/apps)!
      * Run `node --version`.  You may have any version of Node greater than 10.  If you don’t have it or have an older version, install a more recent version of Node.
      * Run `npm --version`.  `npm` is installed with Node, so check that it’s there. If you don’t have it, install a more recent version of Node:
      * Run `git --version`   Check to make sure you have git installed.  

 3. Initiate Heroku.
 
      * Run `heroku create` to create your heroku app. Take note of the info that pops up in the terminal, especially the URL that looks like  http://xxxxxxxxx.herokuapp.com/ That's the URL for your dashboard!

 3. Add in your Alchemy API Key.

      > Change the Alchemy API Key in `main.py` to reflect your particular Alchemy auth token!  We recommend that you set this key in your environment variables. 
       
To set the API key in Heroku's environment variables, run: `heroku config:set KEY="<YOUR ALCHEMY KEY>"`
      
Don't forget to sign into your Alchemy account to use the Transfers API.  See https://docs.alchemy.com/alchemy/documentation/apis/enhanced-apis/transfers-api for more specific documentation.  

If you don’t already have an Alchemy account, [you’ll first need to create one](https://alchemy.com/?r=affiliate:ba2189be-b27d-4ce9-9d52-78ce131fdc2d). The free version will work fine for getting started.  First, we create an App for our Dashboard by clicking “Create App” under the Apps dropdown menu.

![webhook_1](https://github.com/pileofscraps/Alchemy-Transfers-Tutorial/blob/master/app.png)
      
Once we have created the app and pointed it towards the appropriate network, we're ready to go and can paste in our key.

 4. Deploy Heroku.

      * Run `git add .`
      * Run `git commit -m "added Alchemy keys"`
      * Run `git push heroku master` to push and deploy your heroku app.
     
🎉 Congratulations on your dApp deployment! Feel free to edit your app, change its behavior, or make the frontend more spiffy!
