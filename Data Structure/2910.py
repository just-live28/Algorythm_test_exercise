dic = {}

n, c = map(int, input().split())
for num in list(map(int, input().split())):
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1

arr = list(dic.items())
arr.sort(key = lambda x : -x[1])
for num, times in arr:
    for _ in range(times):
        print(num, end=' ')