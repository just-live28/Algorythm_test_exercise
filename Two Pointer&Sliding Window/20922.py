N, K = map(int, input().split())
arr = list(map(int, input().split()))

counts = [0] * 100001
counts[arr[0]] += 1
result = 0
en = 0
for st in range(N):
    while en < N-1 and counts[arr[en + 1]] + 1 <= K:
        en += 1
        counts[arr[en]] += 1
    
    result = max(result, en - st + 1)
    counts[arr[st]] -= 1

print(result)