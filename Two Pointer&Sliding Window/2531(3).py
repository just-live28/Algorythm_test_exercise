N, d, k, c = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.extend(arr)

dishes = [0] * (d+1)
kind_count = 0
for i in range(k):
    dishes[arr[i]] += 1
    if dishes[arr[i]] == 1:
        kind_count += 1

max_kind = kind_count
if dishes[c] == 0:
    max_kind += 1

for st in range(1, N):
    del_dish = arr[st-1]
    
    dishes[del_dish] -= 1
    if dishes[del_dish] == 0:
        kind_count -= 1
    
    add_dish = arr[st + k - 1]
    dishes[add_dish] += 1
    if dishes[add_dish] == 1:
        kind_count += 1
    
    if dishes[c] == 0:
        max_kind = max(max_kind, kind_count + 1)
    else:
        max_kind = max(max_kind, kind_count)

print(max_kind)