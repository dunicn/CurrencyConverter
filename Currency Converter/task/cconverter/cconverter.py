import _json
import requests
import numpy as np


my_currency = input().upper()

cache = {}
r = requests.get(f'http://www.floatrates.com/daily/{my_currency.lower()}.json').json()
# print(r['usd']['rate'])
if my_currency.lower() == 'usd':
    cache.update({'eur': r['eur']})
elif my_currency.lower() == 'eur':
    cache.update({'usd': r['usd']})
else:
    cache.update({'eur': r['eur']})
    cache.update({'usd': r['usd']})

while my_currency:
    desired_currency = input().upper()
    if desired_currency:
        my_money = float(input())
        try:
            if desired_currency.lower() in cache:
                print("Checking the cache…")
                print("Oh! It is in the cache!")
                exchange_rate = cache[desired_currency.lower()]['rate']
                print(f"You received {np.round(my_money * exchange_rate, 2)} {desired_currency.upper()}.")
            else:
                r = requests.get(f'http://www.floatrates.com/daily/{my_currency.lower()}.json').json()
                cache[str(desired_currency.lower())] = r[str(desired_currency.lower())]
                exchange_rate = cache[desired_currency.lower()]['rate']
                print("Checking the cache…")
                print("Sorry, but it is not in the cache!")
                print(f"You received {np.round(my_money * exchange_rate, 2)} {desired_currency.upper()}.")
        except EOFError:
            break
    else:
        break
