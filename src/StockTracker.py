import json
import urllib3
import certifi
import datetime
import unittest
import numbers
from time import sleep


class StockTracker:
    # Setting the license key for AlphaVantage
    apiKey = '2N4O1OBLGVB0P50X'
    # Set the URL for getting stock history data
    stockIntraDayUrl = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={0}&interval=1min&apikey={1}'
    timestamp = 0

    def __init__(self, symbol):
        self.symbol = symbol
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
            if self.symbol == "TestCase1":
                # Make sure to use static data for testing purposes
                with open('../etc/StockTrackerTestData') as f:
                    read_data = f.read()
                self.data = json.loads(read_data)
            else:
                # Use real data from AlphaVantage if not testing
                r = self.http.request('GET', self.stockIntraDayUrl)
                self.data = json.loads(r.data.decode('utf-8'))
            try:
                self.data["Meta Data"]
            except KeyError:
                raise Exception(self.symbol, self.data)
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


class TestStockTracker(unittest.TestCase):

    def setUp(self):
        self.s = StockTracker('TestCase1')

    def test_basic_functions(self):
        m = self.s.show()
        self.assertEqual(m["2. Symbol"], 'MSFT')
        self.assertEqual(m["4. Interval"], '1min')
        self.assertEqual(m["1. Information"], 'Intraday (1min) prices and volumes')
        self.assertTrue(isinstance(self.s.lastAveragePrice(), numbers.Real))
        self.assertEqual(self.s.lastAveragePrice(), 107.8116, 'Not correct last average price calculation')

    def test_refresh(self):
        ts = self.s.timestamp
        self.assertNotEqual(self.s.timestamp, 0, 'StockTracker initialized without data')
        self.s.refresh()
        self.assertEqual(ts, self.s.timestamp, 'StockTracker always refreshing, but should not')
        sleep(61)
        self.s.refresh()
        self.assertNotEqual(ts, self.s.timestamp, 'StockTracker not updating after one minute of waiting')

    def tearDown(self):
        pass


# Run test cases when initializing from CLI
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStockTracker)
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
