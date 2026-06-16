import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit(1)

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            timeout=10,
        )
        response.raise_for_status()
        price = float(response.json()["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError):
        print("Error")
        return

    total = amount * price
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()
