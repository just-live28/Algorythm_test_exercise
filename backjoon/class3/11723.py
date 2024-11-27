# 비트 마스킹

import sys
input = sys.stdin.readline

s = 0

for _ in range(int(input())):
    line = input().split()
    
    if line[0] == 'add':
        s |= (1 << int(line[1]))
    elif line[0] == 'remove':
        s &= ~(1 << int(line[1]))
    elif line[0] == 'check':
        if s & (1 << int(line[1])):
            print(1)
        else:
            print(0)
    elif line[0] == 'toggle':
        s ^= (1 << int(line[1]))
    elif line[0] == 'all':
        s = (1 << 21) - 1
    elif line[0] == 'empty':
        s = 0