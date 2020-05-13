import requests, os, re, time

#Request bitcoin price
def getPrice():
    while True:
        btc_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        timeRegex = re.compile(r'\d\d:\d\d BST')
        time_BST = timeRegex.search(btc_data.text) #Time in BST when price when checked

        priceRegex = re.compile(r'(\d?,\d\d\d.\d\d)')
        prices = priceRegex.findall(btc_data.text)
        USD = prices[0]
        GBP = prices[1]
        EUR = prices[2]

        print(f"At {time_BST.group()} the price of BTC is ${USD}, £{GBP} and €{EUR}")
        time.sleep(10)

getPrice()