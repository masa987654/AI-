import requests

res = requests.get("https://api.coincheck.com/api/ticker")
data = res.json()

price = data["last"]

print("BTC価格:", price)
