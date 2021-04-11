import requests


my_currency = input().lower()
response = requests.get(f'http://www.floatrates.com/daily/{my_currency}.json')
res = response.json()

dollar_rate = 0
euro_rate = 0
if my_currency == 'usd':
    pass
else:
    dollar_rate = res['usd']['rate']
if my_currency == 'eur':
    pass
else:
    euro_rate = res['eur']['rate']

exchange_rate = {"usd": dollar_rate, "eur": euro_rate}

exchange_currency = input().lower()
while True:
    if exchange_currency == "":
        break
    money = float(input())
    else:
        print("Checking the cache...")
        if exchange_currency not in exchange_rate.keys():
            print("Sorry, but it is not in the cache!")
            print(f"You received {round(res[exchange_currency]['rate'] * money,2)} {exchange_currency.upper()}.")
        else:
            print("Oh! It is in the cache!")
            print(f"You received {round(res[exchange_currency]['rate'] * money,2)} {exchange_currency.upper()}.")
    
    exchange_currency = input().lower()
