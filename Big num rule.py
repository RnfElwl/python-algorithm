n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]
count, sum = 0, 0
for i in range(m):
    count += 1
    if count%(k+1) == 0:
        sum += second

    else:
        sum += first

    print(sum)

print(sum)