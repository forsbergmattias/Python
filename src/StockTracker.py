import json
import urllib3
import certifi
import datetime


class StockTracker:
    # Setting the license key for AlphaVantage
    apiKey = '2N4O1OBLGVB0P50X'
    # Set the URL for getting stock history data
    stockIntraDayUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval=1min&apikey={1}'
    timestamp = 0

    def __init__(self, symbol):
        self.stockIntraDayUrl = self.stockIntraDayUrl.format(symbol, self.apiKey)
        self.http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where()
            )
        self.refresh()

    def refresh(self):
        # Make sure that we don't refresh more often than necessary
        ts = datetime.datetime.now().timestamp()
        if (ts-self.timestamp) > 60:
            # Debug purpose print to verify that we only refresh when necessary
            # print("Refreshing...")
            r = self.http.request('GET', self.stockIntraDayUrl)
            self.data = json.loads(r.data.decode('utf-8'))
            self.timestamp = datetime.datetime.now().timestamp()
        else:
            return()

    def show(self):
        self.refresh()
        return(self.data["Meta Data"])

    def lastAveragePrice(self):
        self.refresh()
        stockData = self.data["Time Series (1min)"]
        sortedStockData = sorted(stockData)
        lastMinute = stockData[sortedStockData[0]]
        return (float(lastMinute["1. open"]) + float(lastMinute["4. close"])) / 2


# This code is for debugging purposes only.
# When the Class is run on it's own this code will execute
if __name__ == "__main__":
    s = StockTracker('SEB-A')
    print(s.stockIntraDayUrl)
    print(s.show())
    print(s.lastAveragePrice())
