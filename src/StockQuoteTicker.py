# Finding a Stock quote can be done here
# https://www.xignite.com/product/global-real-time-stock-quote-data/#/DeveloperResources/request/GetGlobalRealTimeQuote
# The JSON URL is
# https://globalrealtime.xignite.com/v3/xGlobalRealTime.json/GetGlobalRealTimeQuote?IdentifierType=Symbol&Identifier=HSBAl.CHIX

import json
import urllib3
import certifi

jsonurl = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=SEK&apikey=2N4O1OBLGVB0P50X'
#jsonurl = 'https://globalrealtime.xignite.com/v3/xGlobalRealTime.json/GetGlobalRealTimeQuote?IdentifierType=Symbol&Identifier=HSBAl.CHIX'
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
response = http.request('GET', jsonurl)
data = json.loads(response.data.decode('utf-8'))
print(data.pop("Meta Data"))

#for date,rates in data.pop("Time Series (Digital Currency Daily)"):
#    print(date + rates)
