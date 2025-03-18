# print(arr[:4] + arr[5:])
# print(len([x for x in arr[:2] + arr[3:] if x > 0]))

n = int(input())
weights = []
stats = []
for _ in range(n):
    s, w = map(int, input().split())
    weights.append(w)
    stats.append(s)

max_count = 0
def func(k, count):
    global max_count
    if k == n:
        max_count = max(max_count, count)
        return
    if stats[k] <= 0:
        func(k+1, count)
    elif len([x for x in stats[:k] + stats[k+1:] if x > 0]) == 0:
        func(k+1, count)
    else:
        for i in range(n):
            if stats[i] <= 0 or i == k:
                continue
            stats[k] -= weights[i]
            stats[i] -= weights[k]
            if stats[i] <= 0 and stats[k] <= 0:
                func(k+1, count+2)
            if stats[i] <= 0 or stats[k] <= 0:
                func(k+1, count+1)
            else:
                func(k+1, count)
            stats[k] += weights[i]
            stats[i] += weights[k]

func(0, 0)
print(max_count)