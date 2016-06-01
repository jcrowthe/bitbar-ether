#!/usr/bin/python
# coding=utf-8

# Provides the latest price of Ether (in USD), pulled from CoinMarketCap
# <bitbar.title>CoinMarketCap Ether latest price</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Jacob Crowther</bitbar.author>
# <bitbar.author.github>jcrowthe</bitbar.author.github>
# <bitbar.desc>Provides the latest price of Ether (in USD), pulled from CoinMarketCap</bitbar.desc>
#
# by Jacob Crowther

import urllib2, json

r = json.loads(urllib2.urlopen('https://coinmarketcap-nexuist.rhcloud.com/api/eth').read())
change = float(r['change'])
if change > 0:
    print 'Ξ', format(r['price']['usd'], '.2f'), '| size=12 color=green'
else:
    print 'Ξ', format(r['price']['usd'], '.2f'), '| size=12 color=red'
print '---'
print 'Change: ', change
