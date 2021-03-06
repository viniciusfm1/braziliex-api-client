# -*- coding: utf-8 -*-
"""
Comunicação com a Exchange de criptomoedas Braziliex através da sua API
Vinícius Machado <viniciusfm1@outlook.com>

    Referências:
        https://braziliex.com/exchange/api.php
"""

import requests
import hmac
import hashlib
import urllib
from time import time

class Braziliex:
    def __init__(self, market, key, secret):
        self.key = key
        self.secret = secret
        self.market = market
        self.privateUrl  = 'https://braziliex.com/api/v1/private'
        self.publicUrl = 'https://braziliex.com/api/v1/public/{command}/{market}'
    
    def post(self, data):
        data['nonce'] = int(time() * 1000)
        data = urllib.parse.urlencode(data).encode('utf-8')
        sign = hmac.new(str.encode(self.secret, 'utf-8'), data, digestmod = hashlib.sha512).hexdigest()
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Sign': sign, 'Key': self.key}
        response = requests.post(self.privateUrl, data = data, headers = headers)
        return response.json()

    def get(self, command):
        response = requests.get(self.publicUrl.format(command = command, market = self.market))
        response.close()
        return response.json()

    def balance(self):      
        """Returns all of your balances, including available balance, balance on orders, 
        and the estimated BTC value of your balance."""
        
        data = {'command': 'balance'}
        return self.post(data)

    def complete_balance(self):
        """Returns all of your balances, including available balance, 
        balance on orders, and the estimated BTC value of your balance."""

        data = {'command': 'complete_balance'}
        return self.post(data)

    def deposit_address(self, currency):
        """Used to get a deposit address by market."""
        data = {'command': 'deposit_address', 'currency': currency}
        return self.post(data)

    def ticker(self):
        """Used to get the current tick values for a market."""
        command = 'ticker'
        return self.get(command)

    def orders(self):
        """Used to get retrieve the orderbook for a given market."""
        command = 'orderbook'
        return self.get(command)

    def trades(self):
        """Used to get retrieve the last trades."""
        command = 'tradehistory'
        return self.get(command)

    def create_order(self, command, amount, price):
        """Places a buy/sell order in a given market"""
        data = {'command': command, 'amount': amount, 'price': price, 'market': self.market}
        return self.post(data)
    
    def cancel_order(self, order_number):
        """Cancels an order you have placed in a given market."""

        data = {'command': 'cancel_order', 'order_number': order_number, 'market': self.market}
        return self.post(data)

    def user_orders(self):
        """Returns your open orders for a given market, 
        specified by the "market" POST parameter, example: ltc_btc"""

        data = {'command':'open_orders', 'market': self.market}
        return self.post(data)

    def history(self):
        """"Returns your trade history for a given market, 
        specified by the "market" POST parameter."""

        data = {'command': 'trade_history', 'market': self.market}
        return self.post(data)