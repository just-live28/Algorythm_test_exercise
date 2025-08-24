import sys
input = sys.stdin.readline

n = int(input())
flowers = []
for _ in range(n):
    st_mon, st_day, en_mon, en_day = map(int, input().split())
    flowers.append((st_mon * 100 + st_day, en_mon * 100 + en_day))

time = 301
result = 0
enable = True
while time < 1201:
    next_time = time
    for st, en in flowers:
        if st <= time and en > next_time:
            next_time = en
    
    if next_time == time:
        enable = False
        break
    
    result += 1
    time = next_time

if enable:
    print(result)
else:
    print(0)