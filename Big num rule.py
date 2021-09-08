
n, m, k = map(int, input().split())

data = list(map(int, input().split()))// n 번 입력받고

data.sort()

first = data[n-1]//가장큰수
second = data[n-2]//두번째로 큰 수
count, sum = 0, 0
for i in range(m): //m번 더해줌
    count += 1
    if count%(k+1) == 0://근데 가장큰수가 k번 넘으면 안됨
        sum += second

    else:
        sum += first

 

print(sum)//큰수의 법칙에 맞는 값 출력
// O(m)의 복잡도가 아닌가?싶다
// 일단 정확한 답이 나오는지 잘 모르겠지만 아마도 맞을것같다
