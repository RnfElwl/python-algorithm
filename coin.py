n = 1200
count = 0

oin_types = [500, 100, 50, 10]

for coin in oin_types:
    count+=n//coin
    n%=coin


print(coin)

