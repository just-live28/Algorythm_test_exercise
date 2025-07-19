n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

diffs = []
for i in range(n-1):
    diffs.append(arr[i+1] - arr[i])
diffs.sort()

for i in range(k-1):
    if diffs:
        diffs.pop()

print(sum(diffs))