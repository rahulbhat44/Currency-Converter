#load the required libraries

from currency_converter import CurrencyConverter #load the library Currency_Converter
from datetime import date #Load the libraries for date and time of extraction
import ccy #Python module for currencies, to get the information about Countries currencies

# get the current rates csv file from the ECB website

current_rates = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

#check the current rates

current_rates._get_rate('USD', date=date(2017, 5, 4))

# We can also Load the history rates as well from the website

history_rates = CurrencyConverter('http://www.ecb.int/stats/eurofxref/eurofxref-hist.zip')

# check the information in detail about the currencies for e.g INR (INDIA)

ccy = ccy.currency('INR')
ccy.printinfo()

#check the currency of the country

ccy.countryccy('us')

# Lets check the rates from current_currency

current_rates.convert(100, 'EUR', 'INR')

#convert the current rate from Euro to INR for today's date

current_rates.convert(100, 'EUR', 'INR', date=date(2017, 5, 4))

# We can also make the default currency, lets make it Euro

current_rates.convert(100, 'EUR')

# Check the rates, how much is 100 Rs in Euro
current_rates.convert(100, 'INR')

#check the history rates

history_rates._get_rate('USD', date=date(2014, 3, 28))

#Fetch the rates form past and convert to INR

history_rates.convert(100, 'EUR', 'INR', date=date(2017, 5, 3))













