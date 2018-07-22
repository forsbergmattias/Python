import json
import urllib3
import certifi

jsonurl = 'https://globalrealtime.xignite.com/v3/xGlobalRealTime.json/GetGlobalRealTimeQuote?IdentifierType=Symbol&Identifier=HSBAl.CHIX'
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where()
)
response = http.request('GET',jsonurl)
data = json.loads(response.data.decode('utf-8'))
print(data.pop("Message"))
