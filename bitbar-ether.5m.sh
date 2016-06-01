#!/bin/bash

# Provides the latest price of Ether (in USD), pulled from CoinMarketCap
# <bitbar.title>CoinMarketCap Ether latest price</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Jacob Crowther</bitbar.author>
# <bitbar.author.github>jcrowthe</bitbar.author.github>
# <bitbar.desc>Provides the latest price of Ether (in USD), pulled from CoinMarketCap</bitbar.desc>
#
# by Jacob Crowther
# Based on Mat Ryer's Coinbase Bitbar plugin

echo -n "Ξ"; curl -s "https://coinmarketcap-nexuist.rhcloud.com/api/eth/price" | egrep -o '"usd":[0-9]+(\.)?([0-9]{0,2})?' | sed 's/"usd"://' | sed 's/\"//g'
