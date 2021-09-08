n = 1200
count = 0

oin_types = [500, 100, 50, 10]

for coin in oin_types:
    count+=n//coin
    n%=coin


print(count)
//oin_types 값이 지금 같은 것이라면 좋지만 oin_types가 500,400,100,10같이 있으면 400 3개가 더 좋은 경우의 수임
