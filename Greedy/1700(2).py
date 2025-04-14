n, k = map(int, input().split())
orders = list(map(int, input().split()))

def find_plug_off_idx(plugs, arr):
    for i in range(n):
        if plugs[i] not in arr:
            return i
    latest = -1
    check = set()
    for i in arr:
        if i in plugs and i not in check:
            latest = i
            check.add(i)
    return plugs.index(latest)

used = 0
plugs = [0] * n
count = 0
for i in range(k):
    if orders[i] in plugs:
        continue
    if used < n:
        plugs[used] = orders[i]
        used += 1
    else:
        idx = find_plug_off_idx(plugs, orders[i+1:])
        plugs[idx] = orders[i]
        count += 1

print(count)