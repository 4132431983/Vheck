import requests

def check_balance(wif_key):
    url = f"https://api.blockcypher.com/v1/btc/main/addrs/{wif_key}/balance"
    response = requests.get(url)
    data = response.json()
    if "balance" in data:
        return data["balance"] > 0
    else:
        return False

with open("keys.txt") as f, open("balance.txt", "w") as out:
    for line in f:
        wif_key = line.strip()
        print(f"Checking balance for WIF key: {wif_key}")
        if check_balance(wif_key):
            print(f"Balance found for WIF key: {wif_key}")
            out.write(wif_key + "\n")
