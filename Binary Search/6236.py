n, m = map(int, input().split())
arr = []
for _ in range(n):
    demand = int(input())
    arr.append(demand)

def cal_withdrawal(arr, target):
    count = 1
    cur = target

    for demand in arr:
        if demand <= cur:
            cur -= demand
            continue

        count += 1
        cur = target
        if demand <= cur:
            cur -= demand
        else:
            return int(1e9)

    return count

min_price = 1
max_price = int(1e9)
result = 0
while (min_price <= max_price):
    mid = (min_price + max_price) // 2

    if cal_withdrawal(arr, mid) <= m:
        result = mid
        max_price = mid - 1
    else:
        min_price = mid + 1

print(result)