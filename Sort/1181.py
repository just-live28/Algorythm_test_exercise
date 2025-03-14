n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))

for i in arr:
    print(i)