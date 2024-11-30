import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

height = [0] * 257
max_height = 256
min_height = 0

for _ in range(n):
    for h in map(int, input().split()):
        height[h] += 1
        max_height = max(max_height, h)
        min_height = min(min_height, h)

min_time = int(1e9)
result_height = 0

for target_height in range(min_height, max_height + 1):
    earn = 0
    need = 0
    time = 0
    
    for i in range(257):
        if height[i] > 0:
            if target_height > i:
                diff = target_height - i
                need += diff * height[i]
                time += diff * height[i]
            elif i > target_height:
                diff = i - target_height
                earn += diff * height[i]
                time += 2 * diff * height[i]
    
    if b + earn >= need:
        if time <= min_time:
            min_time = time
            result_height = target_height

print(min_time, result_height)