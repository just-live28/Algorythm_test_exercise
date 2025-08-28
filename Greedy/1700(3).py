n, k = map(int, input().split())
plans = list(map(int, input().split()))

def find_plug_off_idx(plugs, plans):
    for i in range(n):
        if plugs[i] not in plans:
            return i
    
    latest = -1
    visited = set()
    for i in plans:
        if i in plugs and i not in visited:
            visited.add(i)
            latest = i
            
    return plugs.index(latest)

result = 0
plugs = []
for i in range(k):
    if plans[i] in plugs:
        continue

    if len(plugs) < n:
        plugs.append(plans[i])
        continue

    target_idx = find_plug_off_idx(plugs, plans[i+1:])
    plugs[target_idx] = plans[i]
    result += 1

print(result)