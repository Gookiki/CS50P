import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("amount", type=float)
args = parser.parse_args()

try:
    info = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=fc4a4f017ddf611d6539874271a3809e2d59a4a1e81815b89f00ea062d19a6cc").json()
    price = float(info["data"]["priceUsd"]) * args.amount
    print(f"{price:.4f}")
except requests.RequestException:
    print("Error")