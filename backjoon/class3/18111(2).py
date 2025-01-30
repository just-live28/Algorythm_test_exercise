n, m, b = map(int, input().split())

height = [0] * 257
max_height = 0
min_height = 257
for _ in range(n):
    for h in map(int, input().split()):
        height[h] += 1
        max_height = max(max_height, h)
        min_height = min(min_height, h)

min_time, result_height = int(1e9), 0
for target in range(min_height, max_height + 1):
    time, need, earn = 0, 0, b
    
    for i in range(min_height, max_height + 1):
        if i > target:
            earn += (i - target) * height[i]
            time += 2 * (i - target) * height[i]
        elif i < target:
            need += (target - i) * height[i]
            time += (target - i) * height[i]
    
    if need > earn:
        continue
    else:
        if time <= min_time:
            min_time = time
            result_height = target

print(min_time, result_height)