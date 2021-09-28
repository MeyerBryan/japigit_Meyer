import sys
import pandas as pd

from alpha_vantage.timeseries import TimeSeries 

API_KEY = 'JD4ZDWJ873CGB6Y4'

def getPrice(symbol):

    try:

        timeSeries = TimeSeries(key=API_KEY, output_format='pandas')

        data, meta_data = timeSeries.get_intraday(symbol=symbol, interval='1min')

        return str(data.tail(1).iloc[0]['4. close'])

    except:

        return "not found"

def main():

    outFile = open('japi.out', 'w')

    while 1:

        userInput = input("Enter Stock Symbol or QUIT to exit: ").upper()

        if (userInput != "QUIT" and userInput!= "quit"):

            serverData = 'The current price of {} is {}\n'.format(userInput, getPrice(userInput))

            print(serverData)

            outFile.write(serverData)
            outFile.write("Stock Quotes retrieved successfully!")

        else:

            sys.exit()

main()
