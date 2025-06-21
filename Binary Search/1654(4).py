# k개의 랜선을 모두 n개의 같은 길이 랜선으로 만들기
# 잘랐을 때 N개 이상으로 만들 수 있는 최대 길이
# 해당 길이로 잘랐을 때 N개 이상인가?

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))
arr.sort()

min_length = 1
max_length = arr[-1]
result = 0
while min_length <= max_length:
    mid = (min_length + max_length) // 2

    count = 0
    for i in arr:
        count += i // mid
    
    if count >= n:
        result = mid
        min_length = mid + 1
    else:
        max_length = mid - 1

print(result)