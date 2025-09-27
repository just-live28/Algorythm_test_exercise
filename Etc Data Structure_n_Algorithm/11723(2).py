# 20개의 배열을 두고, 해당 수가 있다면 1, 없다면 0
import sys
input = sys.stdin.readline

m = int(input())
cur = 0
for _ in range(m):
    line = input().split()
    
    if len(line) > 1:
        num = int(line[1])
    
    if line[0] == 'add':
        cur |= (1 << (num-1))
    elif line[0] == 'remove':
        cur &= (~(1 << (num-1)))
    elif line[0] == 'check':
        if cur & (1 << (num-1)):
            print(1)
        else:
            print(0)
    elif line[0] == 'toggle':
        cur ^= (1 << (num-1))
    elif line[0] == 'all':
        cur = (1 << 20) - 1
    elif line[0] == 'empty':
        cur = 0