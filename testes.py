from braziliex import Braziliex
import datetime

exchange = Braziliex('ltc_brl')

ticker = exchange.ticker()

print(ticker)