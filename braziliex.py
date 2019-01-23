# -*- coding: utf-8 -*-
"""
Comunicação com a Exchange de criptomoedas Braziliex através da sua API
Vinícius Machado <viniciusfm1@outlook.com>

    Referências:
        https://braziliex.com/exchange/api.php
"""

import requests
import datetime

class Braziliex:
    def __init__(self, par):
        self.par = par
        self.url = 'https://braziliex.com/api/v1/public/{method}/{param}'
    
    def ticker(self, method = 'ticker'):
        
        """ Used to get the current tick values for a market."""

        response = requests.get(self.url.format(method = method, param = self.par))
        return response.json()

    def orders(self):
        pass

    def trades(self):
        pass