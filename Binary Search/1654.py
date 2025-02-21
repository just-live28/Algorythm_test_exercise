import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
lines.sort()

def get_x_line(lines, x):
    count = 0
    for line in lines:
        count += line // x
    return count

start = 1
end = lines[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    if get_x_line(lines, mid) >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)