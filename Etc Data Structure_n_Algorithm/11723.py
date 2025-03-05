import sys
input = sys.stdin.readline

def add(stat, x):
    return stat | (1 << (x-1))

def remove(stat, x):
    return stat & (~(1 << (x-1)))

def check(stat, x):
    return (stat >> (x-1)) & 1

def toggle(stat, x):
    return stat ^ (1 << (x-1))

stat = 0
m = int(input())
for _ in range(m):
    oper = input().rstrip().split()
    if oper[0] == 'add':
        stat = add(stat, int(oper[1]))
    elif oper[0] == 'remove':
        stat = remove(stat, int(oper[1]))
    elif oper[0] == 'check':
        print(check(stat, int(oper[1])))
    elif oper[0] == 'toggle':
        stat = toggle(stat, int(oper[1]))
    elif oper[0] == 'all':
        stat = 2**20 - 1
    elif oper[0] == 'empty':
        stat= 0