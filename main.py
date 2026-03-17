import requests

res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = res.json()

price = data["bpi"]["USD"]["rate"]

print("BTC価格:", price)
