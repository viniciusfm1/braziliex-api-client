from braziliex import Braziliex
import datetime

exchange = Braziliex('ltc_brl')

ticker = exchange.ticker()
orders = exchange.orders()
trades = exchange.trades()

print('# TICKER #------------------------------')
if ticker['active'] == 1:
    print('última negociação :',ticker['last'])
    print('volume 24h        :',ticker['baseVolume24'])
    print('compra            :',ticker['highestBid'])
    print('venda             :',ticker['lowestAsk'])

print (trades)


