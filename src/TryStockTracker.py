from StockTracker import StockTracker

s = StockTracker('SEB-A')
print(s.stockIntraDayUrl)
print(s.show())
print(s.lastAveragePrice())

s = StockTracker('TestCase1')
print(s.stockIntraDayUrl)
print(s.show())
print(s.lastAveragePrice())
