n, k = map(int, input().split())
orders = list(map(int, input().split()))
    
def find_unplug_candidate(plugs, remain_orders):
    least_order_idx = -1
    idx = 0
    for i in range(n):
        if plugs[i] not in remain_orders:
            return i
        next_order_idx = remain_orders.index(plugs[i])
        if next_order_idx > least_order_idx:
            least_order_idx = next_order_idx
            idx = i
    return idx

def find_space(plugs):
    for i in range(n):
        if plugs[i] == 0:
            return i
    return -1

plugs = [0] * n
count = 0
for o in range(k):
    if orders[o] in plugs:
            continue
    idx = find_space(plugs)
    if idx == -1:
        count += 1
        idx = find_unplug_candidate(plugs, orders[o+1:])
        plugs[idx] = orders[o]
    else:
        plugs[idx] = orders[o]
    
print(count)