import requests
from datetime import datetime, timedelta

STOCK_NAME = "GOOGL"

STOCK_API_KEY = "YG3NLMPB8ZA2QJVU"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=params)
response.raise_for_status()

data = response.json()
data = data["Time Series (Daily)"]

today = datetime.today()

delta = [1, 2]

while True:
    yesterday = (today - timedelta(delta[0])).strftime("%Y-%m-%d")
    before_yesterday = (today - timedelta(delta[1])).strftime("%Y-%m-%d")

    if yesterday not in data:
        delta[0] += 1
        continue

    if before_yesterday not in data:
        delta[1] += 1
        continue

    diff = round(float(data[before_yesterday]["4. close"]) - float(data[yesterday]["4. close"]), 3)
    if 0 <= diff:
        print(f"Up! {diff}$")
    else:
        print(f"Down! {-diff}$")
    break
