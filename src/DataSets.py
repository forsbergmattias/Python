mydata = {
        "2018-07-20 16:00:00": {
            "1. open": "106.3150",
            "2. high": "106.3600",
            "3. low": "106.1700",
            "4. close": "106.2700",
            "5. volume": "4632648"
        },
        "2018-07-20 15:59:00": {
            "1. open": "106.3850",
            "2. high": "106.3900",
            "3. low": "106.3100",
            "4. close": "106.3150",
            "5. volume": "324532"
        },
        "2018-07-20 15:58:00": {
            "1. open": "106.3662",
            "2. high": "106.4300",
            "3. low": "106.3600",
            "4. close": "106.3850",
            "5. volume": "305967"
        }}

#for item in mydata:
#    print(item, "matches", mydata[item])

sortedData = sorted(mydata, reverse=True)
print(mydata[sortedData[0]])
print(len(sortedData))
lastMinute = mydata[sortedData[0]]
lastPrice = (float(lastMinute["1. open"]) + float(lastMinute["4. close"])) / 2
print(lastPrice)
