n, c = map(int, input().split())
arr = list(map(int, input().split()))

hash = {}
for i in range(n):
    num = arr[i]
    if num not in hash:
        hash[num] = [i, 1]
    else:
        hash[num][1] += 1

result = list(hash.items())
result.sort(key = lambda x : (-x[1][1], x[1][0]))
for num, info in result:
    _, count = info
    
    for i in range(count):
        print(num, end=' ')