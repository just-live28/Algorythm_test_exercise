import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.extend(arr)

dishes = {}
result = 0
for i in range(k):
    dish = arr[i]
    
    if dish not in dishes:
        dishes[dish] = 1
        result += 1
    else:
        dishes[dish] += 1

types = result
if c not in dishes:
    result += 1
for st in range(1, N):
    remove_dish = arr[st-1]
    dishes[remove_dish] -= 1
    if dishes[remove_dish] == 0:
        del dishes[remove_dish]
        types -= 1
    
    added_dish = arr[st + k -1]
    if added_dish not in dishes:
        dishes[added_dish] = 1
        types += 1
    else:
        dishes[added_dish] += 1

    if c not in dishes:
        result = max(result, types + 1)
    else:
        result = max(result, types)

print(result)