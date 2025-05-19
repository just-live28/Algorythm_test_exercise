n = int(input())
arr = list(map(int, input().split()))

sorted_arr = sorted(list(set(arr)))
rank = {}
for i in range(len(sorted_arr)):
    rank[sorted_arr[i]] = i

for i in arr:
    print(rank[i], end=' ')