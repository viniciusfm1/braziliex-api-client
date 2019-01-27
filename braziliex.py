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
    def __init__(self, par, key, secret):
        self.par = par
        self.url = 'https://braziliex.com/api/v1/public/{method}/{param}'
        self.key = key
        self.secret = secret
        self.privateUrl  = 'https://braziliex.com/api/v1/private'
    
    def ticker(self, method = 'ticker'):
        
        """Used to get the current tick values for a market."""

        response = requests.get(self.url.format(method = method, param = self.par))
        return response.json()

    def orders(self, method = 'orderbook'):
        
        """Used to get retrieve the orderbook for a given market."""

        response = requests.get(self.url.format(method = method, param = self.par))
        return response.json()

    def trades(self, method = 'tradehistory'):
        """Used to get retrieve the last trades."""
        response = requests.get(self.url.format(method = method, param = self.par))
        return response.json()

    def balance(self, command='balance'):      

        """Returns all of your balances, including available balance, balance on orders, 
        and the estimated BTC value of your balance."""

        data = urllib.parse.urlencode({'command': command, 'nonce': int(time() * 1000)}).encode('utf-8')
        sign = hmac.new(str.encode(self.secret, 'utf-8'), data, digestmod = hashlib.sha512).hexdigest()
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Sign': sign, 'Key': self.key}
        response = requests.post(self.privateUrl, data = data, headers = headers)
        return response.json()

    def buy(self, amount, price):
        
        """Places a buy order in a given market."""
        
        data = urllib.parse.urlencode({'command': 'buy', 'amount': amount, 'price': price, market: self.par, 'nonce': int(time() * 1000)}).encode('utf-8')
        sign = hmac.new(str.encode(self.secret, 'utf-8'), data, digestmod = hashlib.sha512).hexdigest()
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Sign': sign, 'Key': self.key}
        response = requests.post(self.privateUrl, data = data, headers = headers)
        return response.json()
        
    def sell(self):
        pass