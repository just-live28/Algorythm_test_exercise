import sys
import math
input = sys.stdin.readline

def cal_check_amount(time, total_time):
    count = 0
    
    for t in time:
        count += total_time // t
        if count >= m:
            return True
    return False

# n 심사대, m 친구들
n, m = map(int, input().split())
time = []
for _ in range(n):
    time.append(int(input()))
time.sort()

min_time = 0
max_time = time[-1] * math.ceil(m / n)

result = 0
while min_time <= max_time:
    mid = (min_time + max_time) // 2
    
    if cal_check_amount(time, mid):
        result = mid
        max_time = mid - 1
    else:
        min_time = mid + 1

print(result)