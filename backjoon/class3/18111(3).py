n, m, b = map(int, input().split())

height = [0] * 257
max_height = 0
min_height = 257
for _ in range(n):
    for j in map(int, input().split()):
        height[j] += 1
        max_height = max(max_height, j)
        min_height = min(min_height, j)

min_time = int(1e9)
result_height = 0
for target in range(min_height, max_height + 1):
    inventory, need, time = b, 0, 0
    for h in range(min_height, max_height + 1):
        if height[h] == 0:
            continue
        
        if h > target:
            inventory += (h - target) * height[h]
            time += (h - target) * height[h] * 2
        elif h < target:
            need += (target - h) * height[h]
            time += (target - h) * height[h]
    # 인벤토리 블럭 개수 - 필요한 블럭 개수가 0 이상이어야 땅 고르기 가능
    if inventory - need >= 0:
        if time <= min_time:
            min_time = time
            result_height = target

print(min_time, result_height)